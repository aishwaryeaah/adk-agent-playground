from google.adk.agents import Agent
from ...tools.iam_analysis_tool import IamAnalysisTool

iam_agent = Agent(
    name="iam_agent",
    model="gemini-2.0-flash",
    description="Analyze IAM roles and permissions",
    tools=[IamAnalysisTool],
    sub_agents=[],
)