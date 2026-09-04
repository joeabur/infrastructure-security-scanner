from scanner.modules.base import info
from scanner.utils.command import run_command

name = "package_audit"

def scan(config):
    evidence = run_command(["trivy", "rootfs", "--scanners", "vuln", "--format", "json", "/"]) or run_command(["apt", "list", "--upgradable"])
    return [info("Package inventory or vulnerability scan attempted", "Trivy or the local package manager was queried without remediation.", evidence or "No supported package tool available", "packages")]
