import psutil
from scanner.core.models import Finding, Severity

name = "process_audit"

def scan(config):
    processes = []
    for process in psutil.process_iter(["pid", "name", "username", "cmdline"]):
        try:
            processes.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return [Finding("PROC-001", "Running processes enumerated", "Process inventory was collected for anomaly review.", Severity.INFO, "process", evidence=processes, affected_asset=config.target, recommendation="Investigate unknown processes and validate executable ownership.", confidence=1.0)]
