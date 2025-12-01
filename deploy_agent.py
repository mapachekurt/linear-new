"""Deploy the Linear skeleton agent to Vertex AI Agent Engine from source files."""

from __future__ import annotations

import os
import sys
from typing import Any, Dict, List

from google.cloud.aiplatform import vertexai


def main() -> None:
    project_id = os.getenv("PROJECT_ID")
    if not project_id:
        raise ValueError("Environment variable PROJECT_ID is required to deploy the agent.")

    location = os.getenv("LOCATION", "us-central1")

    vertexai.init(project=project_id, location=location)
    client = vertexai.Client(project=project_id, location=location)

    source_packages: List[str] = [
        "linear_agent",
        "requirements.txt",
    ]

    entrypoint_module = "linear_agent.agent"
    entrypoint_object = "root_agent"

    class_methods: List[Dict[str, Any]] = [
        {
            "name": "ping_linear",
            "api_mode": "",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Optional message to echo through ping_linear.",
                    }
                },
                "required": [],
            },
        },
    ]

    config: Dict[str, Any] = {
        "display_name": "Linear ADK Skeleton Agent",
        "description": "Minimal Linear skeleton agent deployed from source files.",
        "source_packages": source_packages,
        "entrypoint_module": entrypoint_module,
        "entrypoint_object": entrypoint_object,
        "class_methods": class_methods,
        "requirements_file": "requirements.txt",
        "agent_framework": "google-adk",
    }

    remote_agent = client.agent_engines.create(config=config)

    print(f"Created agent: {remote_agent.name}")
    operation_schemas = getattr(remote_agent, "operation_schemas", None)
    if operation_schemas:
        print("Available operation schemas:")
        for schema in operation_schemas:
            print(f"- {schema}")
    else:
        print("No operation schemas reported for this agent.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover - deployment helper
        print(f"Deployment failed: {exc}", file=sys.stderr)
        raise
