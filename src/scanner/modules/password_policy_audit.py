from pathlib import Path
from scanner.core.models import Finding, Severity

name = "password_policy_audit"

def scan(config):
    path = Path("/etc/login.defs")
    evidence = {}
    if path.exists():
        for line in path.read_text(errors="replace").splitlines():
            parts = line.split()
            if parts and parts[0] in {"PASS_MAX_DAYS", "PASS_MIN_DAYS", "PASS_MIN_LEN"} and len(parts) > 1:
                evidence[parts[0]] = parts[1]
    weak = "PASS_MAX_DAYS" in evidence and int(evidence["PASS_MAX_DAYS"]) > 365
    return [Finding("PASS-001", "Password aging policy is weak", "Passwords may remain valid for an excessive period.", Severity.MEDIUM, "identity", evidence=evidence, affected_asset=config.target, recommendation="Set password aging according to organizational policy.", confidence=.9)] if weak else [Finding("PASS-002", "Password policy reviewed", "Selected local password policy values were collected.", Severity.INFO, "identity", evidence=evidence, affected_asset=config.target, recommendation="Validate policy against your identity standard.", confidence=.8)]
