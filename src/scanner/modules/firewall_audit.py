from scanner.modules.base import info
from scanner.utils.command import run_command

name = "firewall_audit"

def scan(config):
    evidence = run_command(["ufw", "status"]) or run_command(["firewall-cmd", "--state"]) or run_command(["iptables", "-S"])
    return [info("Firewall status collected", "Firewall tooling was queried without changing system state.", evidence or "No supported firewall command available", "firewall")]
