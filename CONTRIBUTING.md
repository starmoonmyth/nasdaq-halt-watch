# Contributing

Thank you for helping improve Nasdaq Halt Watch.

## Before opening an issue

Search existing issues and include the feed URL, UTC timestamp, parser output,
and a small redacted RSS fixture when reporting a parsing problem. Never post
API keys, credentials, private repository content, or brokerage information.

## Pull requests

1. Keep the library focused on official Nasdaq halt events.
2. Add or update tests for every behavior change.
3. Preserve source timestamps and avoid inferring a halt from missing prices.
4. Run `pytest` and `ruff check .` locally.
5. Explain compatibility or data-contract changes in the PR description.

The project does not provide investment advice or execute trades.

