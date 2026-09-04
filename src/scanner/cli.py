import argparse
import os
from pathlib import Path

from scanner.core.config import ScanConfig
from scanner.core.engine import ScannerEngine
from scanner.registry import MODULES
from scanner.reporters import REPORTERS
from scanner.scoring.risk import score_findings


def main(argv=None):
    parser = argparse.ArgumentParser(prog="scanner", description="Read-only Linux infrastructure security scanner")
    parser.add_argument("--target", default="localhost")
    parser.add_argument("--format", choices=REPORTERS, default="terminal", dest="output_format")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--modules", help="Comma-separated module names")
    parser.add_argument("--no-info", action="store_true", help="Hide informational findings")
    args = parser.parse_args(argv)
    config = ScanConfig(target=args.target, output_format=args.output_format, output_path=args.output, modules=args.modules.split(",") if args.modules else None, include_info=not args.no_info)
    findings = score_findings(ScannerEngine(MODULES, config).scan(), config.asset_criticality)
    if not config.include_info:
        findings = [finding for finding in findings if finding.severity.value != "INFO"]
    output = REPORTERS[config.output_format](findings)
    if args.output:
        output_path = args.output.resolve()
        try:
            output_path.relative_to(Path.cwd().resolve())
        except ValueError:
            parser.error("--output must be inside the current working directory")
        if output_path.is_symlink() or output_path.is_dir():
            parser.error("--output must name a regular report file")
        flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = os.open(output_path, flags, 0o600)
        with os.fdopen(descriptor, "w", encoding="utf-8") as report_file:
            report_file.write(output)
    else:
        print(output)
    return 0


if __name__ == "__main__":
    main()
