# Nasdaq Halt Watch

An open-source monitor for Nasdaq Trader's official trading-halt RSS feed.

It polls no more than once per minute, normalizes halt/resumption records, and
emits de-duplicated events for downstream notifications. It is deliberately
not a market-data feed, trading system, or price-based halt detector.

## Scope

- Current and historical Nasdaq Trader halt RSS records
- Explicit halt and resumption state transitions
- Source timestamps, raw payload retention hooks, and deterministic event IDs
- Library-first API; notification adapters can be added separately

Nasdaq says the feed is updated once per trading minute and asks consumers not
to query it more frequently. See the [official feed documentation](https://www.nasdaqtrader.com/Trader.aspx?id=TradeHaltRSS).

## Status

Early MVP: parser, normalized event model, polling cadence guard, and state
deduplication are being built first. No investment advice or automated order
execution is included.

See [project readiness](docs/PROJECT_READINESS.md) for the public boundary and
[the Codex for OSS application draft](docs/CODEX_FOR_OSS_APPLICATION.md) for
the maintainer-support application materials.

## Development

```bash
python -m pip install -e '.[dev]'
pytest
```
