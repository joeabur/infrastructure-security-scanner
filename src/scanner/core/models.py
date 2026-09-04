from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Dict, List


class Severity(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"


@dataclass
class Finding:
    finding_id: str
    title: str
    description: str
    severity: Severity
    category: str
    evidence: Any = None
    affected_asset: str = "localhost"
    risk: float = 0.0
    recommendation: str = ""
    references: List[str] = field(default_factory=list)
    compliance_mappings: Dict[str, List[str]] = field(default_factory=dict)
    exploitability: float = 0.5
    asset_criticality: float = 0.5
    exposure: float = 0.5
    confidence: float = 0.8

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        result["severity"] = self.severity.value
        return result
