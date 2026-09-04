import platform
from scanner.core.models import Finding, Severity

name = "system_information"

def scan(config):
    return [Finding("SYS-001", "System inventory collected", "Basic host metadata was collected for the assessment.", Severity.INFO, "system", evidence={"hostname": platform.node(), "system": platform.system(), "release": platform.release()}, affected_asset=config.target, recommendation="Keep host inventory current.", confidence=1.0)]
