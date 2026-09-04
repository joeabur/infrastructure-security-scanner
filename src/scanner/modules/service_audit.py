from scanner.modules.base import info
from scanner.utils.command import run_command

name = "service_audit"

def scan(config):
    evidence = run_command(["systemctl", "list-units", "--type=service", "--state=running", "--no-pager"])
    return [info("Running services collected", "Active system services were queried read-only.", evidence or "systemctl unavailable", "services")]
