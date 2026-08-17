from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class HaltState(StrEnum):
    HALTED = "halted"
    RESUMED = "resumed"


@dataclass(frozen=True)
class HaltRecord:
    symbol: str
    issue_name: str | None
    market: str | None
    reason_code: str | None
    halt_time: datetime | None
    resumption_quote_time: datetime | None
    resumption_trade_time: datetime | None
    source_url: str
    source_published_at: datetime | None
    raw_id: str

    @property
    def key(self) -> str:
        return f"{self.symbol}:{self.halt_time.isoformat() if self.halt_time else self.raw_id}"


@dataclass(frozen=True)
class HaltEvent:
    event_id: str
    state: HaltState
    record: HaltRecord
    observed_at: datetime

