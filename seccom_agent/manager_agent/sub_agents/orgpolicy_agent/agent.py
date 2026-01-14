# orgpolicy_agent.py
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

from ...tools.analyze_org_policy_tool import AnalyzeOrgPolicyTool

APP_NAME = "orgpolicy_agent_app"
USER_ID = "user1234"
SESSION_ID = "1234"
MODEL_ID = "gemini-2.0-flash"

# Define the Agent
orgpolicy_agent = Agent(
    model=MODEL_ID,
    name="orgpolicy_agent",
    instruction="""
You are an agent that analyzes GCP organization policies.
Use the 'analyze_org_policy' tool to perform analysis for a given project.
After analysis, provide the user with the findings.
""",
    tools=[AnalyzeOrgPolicyTool]
)

# Async runner setup
async def run_agent(project_id: str):
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
    runner = Runner(agent=orgpolicy_agent, app_name=APP_NAME, session_service=session_service)

    # Create user message content
    content = types.Content(
        role="user",
        parts=[types.Part(text=f"Analyze org policy for project: {project_id}")]
    )

    # Run the agent
    events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    for event in events:
        if event.is_final_response():
            print("Agent Response:", event.content.parts[0].text)
