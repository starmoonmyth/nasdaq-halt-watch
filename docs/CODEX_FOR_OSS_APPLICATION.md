# Codex for OSS application draft

This is a draft for the official OpenAI application form. Replace bracketed
fields with verified repository metrics before submitting.

## Project

**Repository:** `https://github.com/starmoonmyth/nasdaq-halt-watch`

**Role:** Primary maintainer

## Why does this repository qualify? (500-character draft)

Nasdaq Halt Watch is an open-source Python library for reliable monitoring of
official Nasdaq Trader halt and scheduled-resumption events. It normalizes
namespaced RSS records, preserves source timestamps, enforces Nasdaq's
once-per-minute refresh guidance, and de-duplicates state changes for alerts.
It is intentionally independent of brokers and price guesses, so other OSS
tools can reuse a trustworthy event layer. Current usage: [stars/downloads]
and active maintenance by the primary maintainer.

## API credits use (500-character draft)

API credits would support public-project maintenance automation: pull-request
review, parser-fixture generation from redacted official RSS samples, release
note and changelog drafting, documentation checks, and CI failure triage. All
generated changes would remain subject to human review and the repository's
tests. Credits would be used only for this open-source project and its public
maintainer workflows, never for brokerage access or automated trading.

## Requested benefits

- API credits for pull-request review, release workflows, and maintainer
  automation
- Six months of ChatGPT Pro with Codex for day-to-day maintenance
- Codex Security consideration after the repository has a stable release and
  the maintainer can verify repository control

## Evidence to collect before submission

- Public repository URL and public GitHub profile
- Stars, forks, releases, and any package download count
- Link to CI workflow and passing status
- Link to issue tracker and contribution documents
- A short explanation of why official halt data is useful to the OSS ecosystem
- OpenAI Organization ID

