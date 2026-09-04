import pwd
from scanner.core.models import Finding, Severity

name = "privilege_audit"

def scan(config):
    privileged = [entry.pw_name for entry in pwd.getpwall() if entry.pw_uid == 0]
    severity = Severity.HIGH if len(privileged) > 1 else Severity.INFO
    return [Finding("PRIV-001", "Privileged accounts reviewed", "Accounts with UID 0 were identified.", severity, "identity", evidence=privileged, affected_asset=config.target, recommendation="Limit UID 0 to the root account and use audited delegation.", confidence=1.0)]
