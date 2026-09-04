from pathlib import Path
from scanner.core.models import Finding, Severity

name = "cron_audit"

def scan(config):
    paths = [Path("/etc/crontab"), Path("/etc/cron.d")]
    evidence = [str(path) for path in paths if path.exists()]
    return [Finding("CRON-001", "Cron configuration reviewed", "System cron locations were checked for scheduled task review.", Severity.INFO, "persistence", evidence=evidence, affected_asset=config.target, recommendation="Review scheduled tasks for unexpected persistence or writable scripts.", confidence=.9)]
