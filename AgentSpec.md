# Linear ADK Skeleton Agent

This repository contains a minimal Google ADK agent for Linear intended to run on Vertex AI Agent Engine. The agent is intentionally lightweight and currently exposes only a single tool, `ping_linear`, that returns a simple message to confirm the service is reachable.

The agent uses the ADK `Agent` class with a Gemini 2.0 model and is wrapped in an `AdkApp` for deployment to Agent Engine. Future iterations will connect to Linear and Slack and add real workflows, but this initial scaffold keeps the behavior deliberately minimal for quick deployment and verification.
