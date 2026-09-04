import csv
import io

def render(findings):
    output = io.StringIO()
    fields = ["finding_id", "title", "severity", "category", "risk", "affected_asset", "description", "recommendation"]
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()
    for finding in findings:
        data = finding.to_dict()
        writer.writerow({field: data.get(field, "") for field in fields})
    return output.getvalue()
