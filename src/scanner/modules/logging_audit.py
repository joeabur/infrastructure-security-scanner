from scanner.modules.base import info
from scanner.utils.command import run_command

name = "logging_audit"

def scan(config):
    evidence = run_command(["journalctl", "--disk-usage", "--no-pager"])
    return [info("Logging configuration collected", "Local journal availability was queried read-only.", evidence or "journalctl unavailable", "logging")]
