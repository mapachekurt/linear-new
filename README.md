# linear-new: Linear skeleton agent

This repository is a minimal Google ADK-style agent for future Linear + Slack integrations. It targets the `mapache-app` project and deploys to Vertex AI Agent Engine using the source-files flow (no staging bucket).

**Included files**: `linear_agent/agent.py` (agent + tool), `deploy_agent.py` (source-package deployment), `requirements.txt`, and this README.

## Setup

```bash
git clone https://github.com/mapachekurt/linear-new.git
cd linear-new

python -m venv .venv
# Windows:
#   .venv\Scripts\activate
# Unix:
#   source .venv/bin/activate

pip install -r requirements.txt
```

- Use Python 3.10+.
- Ensure `gcloud auth application-default login` has been run for your GCP account.

## Deploy (source packages, no GCS bucket)

Set your environment variables and run the deploy helper:

```bash
export PROJECT_ID="mapache-app"   # or your project
export LOCATION="us-central1"     # optional, defaults to us-central1

python deploy_agent.py
```

The script packages `linear_agent` and `requirements.txt`, registers `linear_agent.agent:root_agent` as the entrypoint, and creates a reasoning engine named "Linear ADK Skeleton Agent".

## Minimal agent details

- Model: `gemini-2.0-flash` (fast Gemini 2.0 model).
- Instruction: "You are a minimal Linear skeleton agent. You only provide a ping_linear tool for basic connectivity tests."
- Tool: `ping_linear(message: Optional[str]) -> str` echoes a provided message or returns a default greeting prefixed with `[linear-new]`.

## Quick remote check (after deploy)

```python
from google.cloud.aiplatform import vertexai

PROJECT_ID = "mapache-app"  # adjust if needed
LOCATION = "us-central1"

client = vertexai.Client(project=PROJECT_ID, location=LOCATION)
remote_agent = client.agent_engines.get(name="projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/<ENGINE_ID>")

async def main():
    async for event in remote_agent.app.async_stream_query(
        user_id="kurt",
        message="Ping the Linear agent",
    ):
        print(event)
```

Replace `<ENGINE_ID>` with the created reasoning engine ID printed by `deploy_agent.py`. This agent intentionally does nothing beyond the ping helper until Linear and Slack features are added.
