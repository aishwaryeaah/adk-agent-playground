from google.adk.tools import FunctionTool, ToolContext

def lookup_cve(query: str, tool_context: ToolContext = None) -> dict:
    """
    Looks up CVEs and vulnerabilities for a given query.

    Args:
        query: The software or component to check.

    Returns:
        dict: CVE results with status
    """
    # dummy data for illustration
    results = [
        {
            "cve_id": "CVE-2025-0001",
            "severity": "HIGH",
            "summary": f"Example CVE matching query '{query}'",
            "mitigation": "Upgrade to patched version"
        }
    ]
    return {"status": "success", "results": results}

LookupCveTool = FunctionTool(func=lookup_cve)
