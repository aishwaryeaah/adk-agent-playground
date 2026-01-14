import os
from google.adk.agents import Agent
from google.adk.tools import ToolContext
from .sub_agents.orgpolicy_agent.agent import orgpolicy_agent
from .sub_agents.Iam_analysing_agent.agent import iam_agent
from .sub_agents.cve_agent.agent import cve_agent

# Read API key from environment
API_KEY = os.environ.get("GOOGLE_API_KEY")

root_agent = Agent(
    name="security_manager",
    model="gemini-2.0-flash",
    description="Root Security Compliance Manager Agent",
    instruction="""
    You are the Security Manager agent. Interpret the user's request and delegate to the appropriate sub-agent(s).
    """,
    sub_agents=[orgpolicy_agent, iam_agent, cve_agent],
    tools=[],
)

