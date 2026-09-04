from scanner.modules.base import info
from scanner.utils.command import run_command

name = "kubernetes_audit"

def scan(config):
    evidence = run_command(["kubectl", "get", "pods", "--all-namespaces", "-o", "json"])
    return [info("Kubernetes configuration check attempted", "Kubernetes resources were queried only when kubectl is available.", evidence or "kubectl unavailable or access denied", "kubernetes")]
