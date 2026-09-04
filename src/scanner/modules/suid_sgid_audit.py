import os
from pathlib import Path
from scanner.core.models import Finding, Severity

name = "suid_sgid_audit"

def scan(config):
    matches = []
    for root in ("/bin", "/sbin", "/usr/bin", "/usr/sbin"):
        path = Path(root)
        if path.exists():
            for item in path.iterdir():
                try:
                    if item.is_file() and item.stat().st_mode & 0o6000:
                        matches.append(str(item))
                except OSError:
                    continue
    return [Finding("SUID-001", "SUID/SGID files enumerated", "Privileged executables were identified for review.", Severity.INFO, "filesystem", evidence=matches, affected_asset=config.target, recommendation="Remove unnecessary SUID/SGID bits and validate ownership.", confidence=.9)]
