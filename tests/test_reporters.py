from scanner.core.models import Finding, Severity
from scanner.reporters import REPORTERS


def test_all_report_formats_render():
    findings = [Finding("T-1", "Title", "Description", Severity.LOW, "test", recommendation="Fix it")]
    assert '"finding_id": "T-1"' in REPORTERS["json"](findings)
    assert "finding_id" in REPORTERS["csv"](findings)
    assert "<table>" in REPORTERS["html"](findings)
    assert "T-1" in REPORTERS["terminal"](findings)
