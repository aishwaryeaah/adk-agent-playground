from google.adk.tools import FunctionTool, ToolContext

def iam_analysis(bindings: list, tool_context: ToolContext = None) -> dict:
    """
    Analyzes IAM role bindings for potential issues.

    Args:
        bindings: List of IAM bindings (dicts with 'role' and 'members').

    Returns:
        dict: {
            "status": "success",
            "results": list of findings
        }
    """
    results = []
    for b in bindings:
        if b.get("role") == "roles/owner":
            results.append({"warning": "Owner role detected", "binding": b})

    # Optionally persist last analyzed bindings
    if tool_context:
        tool_context.state["last_iam_bindings"] = bindings

    return {"status": "success", "results": results}

IamAnalysisTool = FunctionTool(func=iam_analysis)
