import os
import stat
from pathlib import Path
from scanner.core.models import Finding, Severity

name = "filesystem_audit"

def scan(config):
    paths = [Path("/etc/passwd"), Path("/etc/shadow"), Path("/etc/sudoers")]
    evidence = {str(path): oct(stat.S_IMODE(path.stat().st_mode)) for path in paths if path.exists()}
    weak = [path for path, mode in evidence.items() if path.endswith(("shadow", "sudoers")) and int(mode, 8) & 0o004]
    return [Finding("FS-001", "Sensitive files are world-readable", "Sensitive system files have broad read permissions.", Severity.HIGH, "filesystem", evidence=weak, affected_asset=config.target, recommendation="Restrict sensitive files to the minimum required users.", confidence=.95)] if weak else [Finding("FS-002", "Sensitive file permissions reviewed", "Targeted sensitive file permissions were checked.", Severity.INFO, "filesystem", evidence=evidence, affected_asset=config.target, recommendation="Continue enforcing least privilege on system files.", confidence=1.0)]
