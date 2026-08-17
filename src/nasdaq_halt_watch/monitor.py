from datetime import UTC, datetime, timedelta
from hashlib import sha256
from urllib.request import Request, urlopen

from .models import HaltEvent, HaltState
from .parser import parse_feed

DEFAULT_FEED_URL = "https://www.nasdaqtrader.com/rss.aspx?feed=tradehalts"


class HaltMonitor:
    """Small stateful monitor. Call poll() at most once per 60 seconds."""

    def __init__(self, feed_url: str = DEFAULT_FEED_URL, min_interval: timedelta = timedelta(minutes=1)):
        self.feed_url = feed_url
        self.min_interval = min_interval
        self._last_poll: datetime | None = None
        self._states: dict[str, HaltState] = {}

    def poll(self, payload: str | bytes | None = None, now: datetime | None = None) -> list[HaltEvent]:
        now = now or datetime.now(UTC)
        if self._last_poll and now - self._last_poll < self.min_interval:
            return []
        self._last_poll = now
        if payload is None:
            request = Request(self.feed_url, headers={"User-Agent": "nasdaq-halt-watch/0.1"})
            with urlopen(request, timeout=15) as response:
                payload = response.read()
        events: list[HaltEvent] = []
        for record in parse_feed(payload, self.feed_url):
            state = HaltState.RESUMED if record.resumption_trade_time else HaltState.HALTED
            if self._states.get(record.key) == state:
                continue
            self._states[record.key] = state
            digest = sha256(f"{record.key}:{state}".encode()).hexdigest()[:24]
            events.append(HaltEvent(digest, state, record, now))
        return events
