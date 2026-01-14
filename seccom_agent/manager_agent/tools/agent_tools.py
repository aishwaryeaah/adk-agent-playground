# tools/tools.py
from google.adk.tools.tool_context import ToolContext
from datetime import datetime
import json

def query_bigquery(query: str, tool_context: ToolContext = None) -> dict:
    """
    STUB: Replace with google-cloud-bigquery client code.
    Returns a dict: {"status":"success","rows":[...]}
    """
    print(f"--- Tool: query_bigquery called ---\n{query}\n---")
    # Basic heuristic stubs for common queries
    q = (query or "").lower()
    if "firewall" in q:
        rows = [
            {"rule": "allow-ssh", "sourceRanges": ["0.0.0.0/0"], "project": "project-a"},
        ]
    elif "iam" in q or "binding" in q:
        rows = [
            {"binding": "allUsers", "role": "roles/storage.objectViewer", "project": "project-b"},
        ]
    else:
        rows = []
    return {"status": "success", "rows": rows, "fetched_at": datetime.utcnow().isoformat()}

def analyze_org_policy(policy_docs: list, tool_context: ToolContext = None) -> dict:
    """
    STUB: policy_docs can be a list of dicts or JSON/YAML strings.
    Return: {"status":"success","findings":[...]}
    """
    print("--- Tool: analyze_org_policy called ---")
    findings = []
    for doc in policy_docs:
        s = doc if isinstance(doc, str) else json.dumps(doc)
        if "*\"allowedValues\"*".replace("*","") in s or "\"*\"" in s:
            findings.append({"issue": "wildcard allowedValues", "doc_preview": s[:200]})
        # naive checks
        if "disable" in s.lower() and "constraint" in s.lower():
            findings.append({"issue": "disabled constraint", "doc_preview": s[:200]})
    return {"status": "success", "findings": findings}

def lookup_cve(query: str, tool_context: ToolContext = None) -> dict:
    """
    STUB: Replace with OSV / NVD / internal CVE DB lookup.
    """
    print(f"--- Tool: lookup_cve called for: {query} ---")
    # fake result example
    return {
        "status": "success",
        "results": [
            {
                "cve_id": "CVE-2025-0001",
                "severity": "HIGH",
                "summary": f"Example CVE matching query '{query}'",
                "mitigation": "Upgrade to patched version"
            }
        ],
    }

def get_current_time(_, tool_context: ToolContext = None) -> dict:
    return {"status": "success", "utc": datetime.utcnow().isoformat()}
