from pathlib import Path
from scanner.core.models import Finding, Severity

name = "ssh_audit"

def scan(config):
    path = Path("/etc/ssh/sshd_config")
    if not path.exists():
        return [Finding("SSH-INFO", "SSH server configuration unavailable", "No local sshd configuration was found.", Severity.INFO, "ssh", affected_asset=config.target, recommendation="Review SSH settings on hosts running an SSH server.", confidence=1.0)]
    text = path.read_text(errors="replace")
    weak = [line.strip() for line in text.splitlines() if line.strip().lower().startswith(("permitrootlogin yes", "passwordauthentication yes"))]
    return [Finding("SSH-001", "Weak SSH settings detected", "The SSH daemon enables one or more high-risk settings.", Severity.HIGH, "ssh", evidence=weak, affected_asset=config.target, recommendation="Prefer key authentication and disable direct root login.", confidence=.95)] if weak else [Finding("SSH-002", "SSH configuration reviewed", "No targeted weak SSH settings were found.", Severity.INFO, "ssh", evidence=str(path), affected_asset=config.target, recommendation="Continue validating SSH settings against policy.", confidence=.8)]
