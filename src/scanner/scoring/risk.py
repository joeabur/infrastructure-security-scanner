from typing import List, Optional

from scanner.core.models import Finding, Severity

SEVERITY_WEIGHT = {Severity.CRITICAL: 1.0, Severity.HIGH: .8, Severity.MEDIUM: .55, Severity.LOW: .3, Severity.INFO: .05}


def score_finding(finding: Finding, asset_criticality: Optional[float] = None) -> float:
    criticality = finding.asset_criticality if asset_criticality is None else asset_criticality
    value = SEVERITY_WEIGHT[Severity(finding.severity)] * finding.exploitability * criticality * finding.exposure * finding.confidence
    finding.risk = round(value * 10, 2)
    return finding.risk


def score_findings(findings: List[Finding], asset_criticality: float = .5) -> List[Finding]:
    for finding in findings:
        score_finding(finding, asset_criticality)
    return findings
