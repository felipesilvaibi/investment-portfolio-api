# icon api-name API

## About

Example api about info.

## Features

Example api features info.

## Getting Started

### Prerequisites

- Python 3.10
- Poetry for dependency management

### Installation and Setup

1. Clone the repository:
```
git clone example_repo
```

2. Navigate to the project directory:
```
cd example_repo
```

3. Install dependencies using Poetry:
```
poetry install
```

### Configuration

Example api secrets and env vars info.

### Running the Service

Using Poetry, you can run the service directly. Ensure you have configured the application correctly, including the environment variables needed.
```
poetry run uvicorn src.main.config.app:app --host 0.0.0.0 --port 8080
```

## Usage
Example Api usage info.

#### Example Payload for a Generic Message
Example json info.

## Docker Deployment
Your provided Dockerfile is set up for a multi-stage build, optimizing dependencies installation and minimizing the final image size. Make sure to build and run your Docker container according to your operational environment requirements.

## CI/CD Configuration
CI/CD Configuration
You've outlined workflows for deployment, Terraform apply, plan, and destroy. Ensure these workflows are configured in your .github/workflows directory, adjusting for your specific project and operational needs.

## Google Cloud Integration

For the current project, we are utilizing Google Cloud to manage the infrastructure. To maximize the project's potential, the following configurations are necessary:

1. **Create a Google Cloud Account**: Begin by signing up for a Google Cloud account if you haven't already.

2. **Activate the Free Tier**: Take advantage of Google Cloud's free tier to access many services without incurring costs.

3. **Enable Necessary APIs**: Activate the following APIs in your Google Cloud project:
   - **Identity and Access Management (IAM) API**: Essential for managing access and identities.
   - **Cloud Resource Manager API**: Required for managing resources.
   - **Secret Manager API**: For storing and accessing secrets safely.
   - **Cloud Run API** (if necessary): If you're deploying applications with Cloud Run.

4. **Service Account for GitHub Actions**: Create a service account to be used by GitHub Actions with the following permissions:
   - Firebase Remote Config Administrator
   - App Engine Service Admin
   - App Engine Admin
   - Cloud Functions Admin
   - Cloud Run Admin
   - Cloud Scheduler Admin
   - Compute Storage Admin
   - Secret Manager Admin
   - Artifact Registry Repository Admin
   - Storage Admin
   - Pub/Sub Admin
   - App Engine Flexible Environment Service Agent
   - App Engine Creator
   - Cloud Build Editor
   - App Engine Deployer
   - Service Account User
   - Service Account Admin

5. **GitHub Actions Secrets**: Access the githubactions service account, generate a `GCP_SA_KEY` in JSON format, and add it to the GitHub repo's actions secrets. Also, add the `GH_TOKEN` (GitHub token) to the repo's secrets.

6. **Cloud Storage Bucket**: Create a bucket in Cloud Storage using the repository name and branch as the naming convention (e.g., `example-api-main`).

7. **Cloud Build Repository Connection**: Create and authenticate a connection with your repository in Cloud Build.

8. **Secret Manager Configuration**: Example api secrets info.

This setup ensures your project is fully integrated with Google Cloud, leveraging its powerful infrastructure and services for optimal performance and scalability.
