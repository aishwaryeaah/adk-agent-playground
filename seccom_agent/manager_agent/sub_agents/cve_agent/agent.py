from google.adk.agents import Agent
from ...tools.lookup_cve_tool import LookupCveTool

cve_agent = Agent(
    name="cve_agent",
    model="gemini-2.0-flash",
    description="Lookup CVEs and vulnerabilities",
    tools=[LookupCveTool],
    sub_agents=[],
)