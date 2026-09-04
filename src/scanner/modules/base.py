import os

from scanner.core.models import Finding, Severity


def info(name: str, description: str, evidence: object, category: str) -> Finding:
    return Finding(f"{category.upper()}-INFO", name, description, Severity.INFO, category, evidence=evidence, recommendation="Review manually when the relevant platform or tool is available.", confidence=1.0)


def check_file(path: str) -> bool:
    return os.path.exists(path)
