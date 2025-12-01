"""Minimal Linear ADK skeleton agent for Vertex AI Agent Engine."""


from google.adk.agents import Agent
from vertexai import agent_engines


def ping_linear(message: str = "Hello from the Linear ADK skeleton agent") -> str:
    """Return a simple string that proves the agent is alive."""
    return f"[linear-adk-skeleton] {message}"


root_agent: Agent = Agent(
    model="gemini-1.5-flash-001",    name="linear_adk_skeleton_agent",
    tools=[ping_linear],
)

app: agent_engines.AdkApp = agent_engines.AdkApp(agent=root_agent, enable_tracing=True)

__all__ = ["ping_linear", "root_agent", "app"]
