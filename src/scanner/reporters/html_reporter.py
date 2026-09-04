import html

def render(findings):
    rows = []
    for finding in findings:
        item = finding.to_dict()
        rows.append("<tr>" + "".join(f"<td>{html.escape(str(item.get(field, '')))}</td>" for field in ("finding_id", "severity", "category", "risk", "title", "recommendation")) + "</tr>")
    return "<!doctype html><html><head><meta charset='utf-8'><title>Infrastructure Security Assessment</title><style>body{font:14px sans-serif;margin:2rem;color:#17202a}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccd;padding:.6rem;text-align:left}th{background:#17202a;color:white}</style></head><body><h1>Infrastructure Security Assessment</h1><table><thead><tr><th>ID</th><th>Severity</th><th>Category</th><th>Risk</th><th>Title</th><th>Recommendation</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table></body></html>"
