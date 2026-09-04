from scanner.modules.base import info
from scanner.utils.command import run_command

name = "docker_audit"

def scan(config):
    evidence = run_command(["docker", "info", "--format", "{{json .SecurityOptions}}"])
    return [info("Docker security configuration collected", "Docker security options were queried when Docker is available.", evidence or "Docker unavailable", "containers")]
