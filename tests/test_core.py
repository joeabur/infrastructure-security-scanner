from scanner.core.config import ScanConfig
from scanner.core.engine import ScannerEngine
from scanner.core.models import Finding, Severity
from scanner.scoring.risk import score_finding


def test_finding_schema_and_risk():
    finding = Finding("T-1", "Example", "Description", Severity.HIGH, "test")
    assert finding.to_dict()["severity"] == "HIGH"
    assert score_finding(finding, 1.0) > 0


def test_engine_continues_after_module_failure():
    class Broken:
        name = "broken"
        def scan(self, config):
            raise RuntimeError("unavailable")
    findings = ScannerEngine([Broken()], ScanConfig()).scan()
    assert findings[0].finding_id == "ENGINE-BROKEN"
