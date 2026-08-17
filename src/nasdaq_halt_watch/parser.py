from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Any

import feedparser

from .models import HaltRecord


def _text(entry: Any, *names: str) -> str | None:
    for name in names:
        value = entry.get(name)
        if value not in (None, ""):
            return str(value).strip()
    return None


def _time(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return parsedate_to_datetime(value)
    except (TypeError, ValueError):
        for fmt in ("%m/%d/%Y %H:%M:%S", "%m/%d/%Y %H:%M"):
            try:
                return datetime.strptime(value, fmt).replace(tzinfo=UTC)
            except ValueError:
                pass
    return None


def _date_time(entry: Any, date_name: str, time_name: str) -> datetime | None:
    date_value = _text(entry, date_name)
    time_value = _text(entry, time_name)
    if not date_value or not time_value:
        return None
    return _time(f"{date_value} {time_value}")


def parse_feed(payload: str | bytes, source_url: str) -> list[HaltRecord]:
    """Parse Nasdaq Trader RSS while preserving unknown fields via raw_id."""
    parsed = feedparser.parse(payload)
    records: list[HaltRecord] = []
    for index, entry in enumerate(parsed.entries):
        symbol = _text(entry, "ndaq_issuesymbol", "issue_symbol", "symbol", "title")
        if not symbol:
            continue
        published = _time(_text(entry, "published", "updated"))
        raw_id = _text(entry, "id", "guid", "link") or f"entry-{index}"
        records.append(HaltRecord(
            symbol=symbol,
            issue_name=_text(entry, "ndaq_issuename", "issue_name", "company_name", "name"),
            market=_text(entry, "ndaq_market", "market", "market_category"),
            reason_code=_text(entry, "ndaq_reasoncode", "reason_code", "halt_code", "category"),
            halt_time=(
                _date_time(entry, "ndaq_haltdate", "ndaq_halttime")
                or _time(_text(entry, "halt_time", "halt_date_time"))
            ),
            resumption_quote_time=(
                _date_time(entry, "ndaq_resumptiondate", "ndaq_resumptionquotetime")
                or _time(_text(entry, "resumption_quote_time"))
            ),
            resumption_trade_time=(
                _date_time(entry, "ndaq_resumptiondate", "ndaq_resumptiontradetime")
                or _time(_text(entry, "resumption_trade_time"))
            ),
            source_url=source_url,
            source_published_at=published,
            raw_id=raw_id,
        ))
    return records
