"""Minimal Linear skeleton agent for Vertex AI Agent Engine."""

from typing import Optional

from google.adk.agents import Agent


DEFAULT_MODEL = "gemini-1.5-flash-001"
DEFAULT_INSTRUCTIONS = (
    "You are a minimal Linear skeleton agent. You only provide a ping_linear tool for basic connectivity tests."
)


def ping_linear(message: Optional[str] = None) -> str:
    """
    Minimal health check tool for the Linear skeleton agent.

    If message is provided, echo it. Otherwise, return a default greeting.
    """
    if not message:
        message = "Hello from the Linear skeleton agent"
    return f"[linear-new] {message}"


root_agent: Agent = Agent(
    model=DEFAULT_MODEL,
    name="linear_new_agent",
    instructions=DEFAULT_INSTRUCTIONS,
    tools=[ping_linear],
)

__all__ = ["ping_linear", "root_agent"]
