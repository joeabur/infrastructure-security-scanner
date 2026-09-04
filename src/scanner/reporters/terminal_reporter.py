def render(findings):
    lines = [f"Infrastructure Security Assessment: {len(findings)} findings"]
    for finding in findings:
        lines.append(f"[{finding.severity.value}] {finding.finding_id} {finding.title} (risk={finding.risk})")
        lines.append(f"  {finding.recommendation}")
    return "\n".join(lines)
