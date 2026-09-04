import json

def render(findings):
    return json.dumps([finding.to_dict() for finding in findings], indent=2, default=str)
