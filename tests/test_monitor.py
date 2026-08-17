from datetime import UTC, datetime, timedelta

from nasdaq_halt_watch import HaltMonitor, HaltState

RSS = """<?xml version='1.0'?><rss><channel><item>
<guid>abc-1</guid><title>XYZ</title><ndaq:IssueSymbol xmlns:ndaq='x'>XYZ</ndaq:IssueSymbol>
<ndaq:IssueName xmlns:ndaq='x'>Example Inc</ndaq:IssueName>
<ndaq:Market xmlns:ndaq='x'>NASDAQ</ndaq:Market>
<ndaq:ReasonCode xmlns:ndaq='x'>T1</ndaq:ReasonCode>
<ndaq:HaltDate xmlns:ndaq='x'>08/17/2026</ndaq:HaltDate>
<ndaq:HaltTime xmlns:ndaq='x'>10:00:00.000</ndaq:HaltTime>
</item></channel></rss>"""


def test_poll_deduplicates_and_respects_interval():
    monitor = HaltMonitor(min_interval=timedelta(minutes=1))
    now = datetime(2026, 8, 17, 14, 0, tzinfo=UTC)
    events = monitor.poll(RSS, now)
    assert len(events) == 1
    assert events[0].state == HaltState.HALTED
    assert monitor.poll(RSS, now) == []
