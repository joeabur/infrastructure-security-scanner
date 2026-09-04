import psutil
from scanner.core.models import Finding, Severity

name = "network_audit"

def scan(config):
    connections = [{"local": f"{c.laddr.ip}:{c.laddr.port}", "status": c.status, "pid": c.pid} for c in psutil.net_connections(kind="inet") if c.laddr]
    exposed = [item for item in connections if item["status"] == "LISTEN"]
    return [Finding("NET-001", "Listening network sockets identified", "Local listening sockets were enumerated.", Severity.INFO, "network", evidence=exposed, affected_asset=config.target, recommendation="Restrict listeners to required interfaces and services.", exposure=.8, confidence=1.0)]
