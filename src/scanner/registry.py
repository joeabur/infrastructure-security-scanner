from scanner.modules import cron_audit, docker_audit, filesystem_audit, firewall_audit, kernel_audit, kubernetes_audit, logging_audit, network_audit, package_audit, password_policy_audit, privilege_audit, process_audit, service_audit, ssh_audit, suid_sgid_audit, system_information, user_audit

MODULES = [system_information, user_audit, privilege_audit, ssh_audit, firewall_audit, network_audit, service_audit, filesystem_audit, suid_sgid_audit, cron_audit, process_audit, package_audit, kernel_audit, docker_audit, kubernetes_audit, logging_audit, password_policy_audit]
