import importlib

import pytest

MODULE_NAMES = ["system_information", "user_audit", "privilege_audit", "ssh_audit", "firewall_audit", "network_audit", "service_audit", "filesystem_audit", "suid_sgid_audit", "cron_audit", "process_audit", "package_audit", "kernel_audit", "docker_audit", "kubernetes_audit", "logging_audit", "password_policy_audit"]


@pytest.mark.parametrize("module_name", MODULE_NAMES)
def test_module_returns_normalized_findings(module_name):
    module = importlib.import_module(f"scanner.modules.{module_name}")
    findings = module.scan(type("Config", (), {"target": "fixture", "command_timeout": 1.0})())
    assert findings
    assert all(hasattr(finding, "finding_id") and hasattr(finding, "severity") for finding in findings)
