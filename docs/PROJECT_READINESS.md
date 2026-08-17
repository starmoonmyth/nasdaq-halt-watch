# Open-source readiness checklist

This document keeps the project boundary explicit for maintainers and program
reviewers.

## Included

- Official Nasdaq Trader halt RSS ingestion
- Normalized halt and scheduled-resumption records
- Source URL and source publication timestamps
- A 60-second minimum polling guard, matching Nasdaq's published guidance
- Deterministic event identifiers and in-process de-duplication
- Tests, CI, issue template, contribution guidance, security policy, and code
  of conduct

## Deliberately excluded

- Brokerage accounts, order placement, portfolio data, or trading signals
- Price-based guesses that a security is halted
- Private API keys or user data
- Investment advice, performance claims, or return guarantees
- Scanning repositories or systems without authorization

## Release gate before 1.0

- Add SQLite persistence and restart recovery
- Add fixture tests for every documented Nasdaq reason/resumption code
- Add structured logging and fetch-health metrics
- Add one notification adapter with explicit opt-in configuration
- Publish a versioned changelog and signed release process

