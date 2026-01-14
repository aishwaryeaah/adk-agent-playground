# analyze_org_policy_tool.py
from google.adk.tools import FunctionTool, ToolContext

def analyze_org_policy(project_id: str, tool_context: ToolContext) -> dict:
    """
    Analyzes organization policies for the given GCP project.

    Args:
        project_id: The GCP project ID to analyze.

    Returns:
        dict: {
            "status": "success" or "error",
            "findings": summary of the policy analysis
        }
    """
    # Placeholder logic: replace with actual org policy calls
    findings = f"Org policy analysis for project '{project_id}' completed successfully."

    # Optionally store the last project analyzed in session state
    tool_context.state["last_project_analyzed"] = project_id

    return {"status": "success", "findings": findings}

# Wrap as a FunctionTool
AnalyzeOrgPolicyTool = FunctionTool(func=analyze_org_policy)
