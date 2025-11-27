# Linear Skeleton Agent (Mapache)

This repository contains a minimal Linear skeleton agent for Mapache. It is intended to run on Vertex AI Agent Engine in the `mapache-app` project using the Google ADK patterns. The agent currently exposes only a `ping_linear` tool used to verify connectivity.

The agent will later integrate with Linear webhooks and Slack slash commands to deliver real workflows. Until then, this scaffold remains small, with a single Gemini-based agent entrypoint and a deployment script that ships source files directly to Agent Engine.
