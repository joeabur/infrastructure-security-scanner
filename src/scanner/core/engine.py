from typing import Iterable, List

from scanner.core.config import ScanConfig
from scanner.core.models import Finding, Severity


class ScannerEngine:
    def __init__(self, modules: Iterable[object], config: ScanConfig):
        self.modules = list(modules)
        self.config = config
        self.config.validate()

    def scan(self) -> List[Finding]:
        findings: List[Finding] = []
        selected = set(self.config.modules or [])
        for module in self.modules:
            name = getattr(module, "name", module.__class__.__name__)
            if selected and name not in selected:
                continue
            try:
                findings.extend(module.scan(self.config))
            except Exception as error:
                findings.append(Finding(
                    finding_id=f"ENGINE-{name.upper()}", title=f"Module {name} failed",
                    description="The audit module could not complete.", severity=Severity.LOW,
                    category="scanner", evidence=str(error), affected_asset=self.config.target,
                    recommendation="Review module logs and rerun with appropriate permissions.",
                    confidence=1.0,
                ))
        return findings
