# Threat model

## Assets

Host identity data, process and network inventories, package details, configuration paths, and generated reports.

## Risks

A scan may expose sensitive host metadata, execute an optional local diagnostic binary, or produce misleading results when run without privileges. Reports may be tampered with if written to an untrusted directory.

## Controls

Read-only checks, no shell execution, command timeouts, safe target validation, HTML escaping, explicit optional-tool behavior, and documentation warning that reports are sensitive. Operators should use least-privileged accounts and protected report storage.
