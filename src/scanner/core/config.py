from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass
class ScanConfig:
    target: str = "localhost"
    modules: Optional[List[str]] = None
    output_format: str = "terminal"
    output_path: Optional[Path] = None
    command_timeout: float = 5.0
    include_info: bool = True
    asset_criticality: float = 0.5

    def validate(self) -> None:
        if not self.target or any(char in self.target for char in ";&|`$\n"):
            raise ValueError("target must be a non-empty safe host identifier")
        if not 0 <= self.asset_criticality <= 1:
            raise ValueError("asset_criticality must be between 0 and 1")
        if self.output_format not in {"json", "csv", "html", "terminal"}:
            raise ValueError("unsupported output format")
