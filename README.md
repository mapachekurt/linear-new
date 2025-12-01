# Linear ADK Skeleton Agent

A minimal Google ADK agent scaffold for Linear that runs on Vertex AI Agent Engine. Behavior is intentionally tiny for initial deployment and smoke testing.

Clone the repo and set up your environment (copy/paste-ready):

```bash
git clone https://github.com/mapachekurt/linear-adk-skeleton.git
cd linear-adk-skeleton

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

## Local setup

1. Use Python 3.10 or 3.11.
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## GCP prerequisites

- Select or create a GCP project.
- Enable the Vertex AI API.
- Ensure a Cloud Storage bucket exists for staging artifacts, for example `gs://YOUR_PROJECT-staging-bucket`.
- Authenticate locally:

  ```bash
  gcloud auth application-default login
  ```

## Deploy to Vertex AI Agent Engine with ADK CLI

The ADK CLI is included via the `google-cloud-aiplatform` extras. From the repository root:

```bash
export PROJECT_ID="your-project-id"
export LOCATION="us-central1"
export STAGING_BUCKET="gs://your-staging-bucket"

adk deploy agent_engine \
    --project=${PROJECT_ID} \
    --region=${LOCATION} \
    --staging_bucket=${STAGING_BUCKET} \
    --display_name="Linear ADK Skeleton Agent" \
    .
```

## Test the deployed agent

After deployment, create a client and stream a simple query to call `ping_linear`:

```python
from vertexai import agent_engines
import asyncio

PROJECT_ID = "your-project-id"
LOCATION = "us-central1"

client = agent_engines.create_client(project=PROJECT_ID, location=LOCATION)
remote_agent = client.get_agent_app(display_name="Linear ADK Skeleton Agent")

async def main():
    async for event in remote_agent.async_stream_query(
        user_id="kurt",
        message="Ping the Linear agent",
    ):
        print(event)

asyncio.run(main())
```

This is intentionally minimal; future iterations will add Linear and Slack integrations.
