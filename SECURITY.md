# Security

The scanner is designed to be read-only. It uses argument-list subprocess execution, bounded timeouts, no shell interpolation, and no embedded credentials. Optional integrations are queried only when their executables are present.

Reports can contain usernames, process command lines, paths, and infrastructure details. Treat generated reports as confidential. Do not submit credentials, secrets, or private keys as scan input.

Report vulnerabilities in this project privately to the maintainers listed in `CODEOWNERS`. Include reproduction steps and affected versions; do not include live secrets.
