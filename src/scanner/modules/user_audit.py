import pwd
from scanner.core.models import Finding, Severity

name = "user_audit"

def scan(config):
    users = [{"name": entry.pw_name, "uid": entry.pw_uid, "shell": entry.pw_shell} for entry in pwd.getpwall()]
    return [Finding("USR-001", "Local users enumerated", "Local account inventory is available for review.", Severity.INFO, "identity", evidence=users, affected_asset=config.target, recommendation="Disable unused accounts and review interactive shells.", confidence=1.0)]
