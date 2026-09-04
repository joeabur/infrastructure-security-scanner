from pathlib import Path
from scanner.core.models import Finding, Severity

name = "kernel_audit"

def scan(config):
    evidence = {}
    for key in ("randomize_va_space", "kptr_restrict", "dmesg_restrict"):
        path = Path("/proc/sys/kernel") / key
        if path.exists():
            evidence[key] = path.read_text().strip()
    weak = [key for key, value in evidence.items() if value in {"0", "-1"}]
    return [Finding("KERNEL-001", "Weak kernel hardening setting", "One or more kernel security controls are disabled.", Severity.MEDIUM, "kernel", evidence=weak, affected_asset=config.target, recommendation="Enable kernel hardening controls according to the host baseline.", confidence=.95)] if weak else [Finding("KERNEL-002", "Kernel settings reviewed", "Selected kernel hardening settings were collected.", Severity.INFO, "kernel", evidence=evidence, affected_asset=config.target, recommendation="Compare settings with your approved baseline.", confidence=.9)]
