# Flask DevOps CI/CD Pipeline

Intermediate portfolio project demonstrating an automated CI/CD workflow for a Python Flask application using Git, GitHub, Jenkins, Docker, and pytest.

## Architecture
Developer push -> GitHub -> Jenkins -> automated tests -> Docker image build -> container smoke test.

## Project structure
- `app/`: Flask application, HTML template, and CSS
- `tests/`: pytest test cases
- `Dockerfile`: production container image
- `Jenkinsfile`: declarative CI/CD pipeline
- `compose.yaml`: local container deployment
- `requirements.txt`: Python dependencies

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python run.py
```
Open http://localhost:5000 and http://localhost:5000/health.

## Run using Docker Compose
```bash
docker compose up --build -d
docker compose ps
docker compose down
```
Open http://localhost:5000. API endpoints: `/health` and `/api/info`.

## Jenkins prerequisites
- Jenkins Linux agent with Docker CLI and access to the Docker daemon
- Git and Jenkins Pipeline plugin
- GitHub repository containing this project
- Port 5000 available on the agent during the smoke test

## Configure Jenkins
1. Push this project to a GitHub repository.
2. In Jenkins select **New Item** -> **Pipeline**.
3. Select **Pipeline script from SCM**, choose Git, and enter the repository URL.
4. Set Script Path to `Jenkinsfile`, then save.
5. Select **Build Now** and inspect the pipeline stages.

The pipeline checks out code, runs pytest in a temporary Python container, builds a Docker image, starts the application container, and checks its `/health` endpoint using a temporary curl container. It removes the test container after execution.

## Scope and limitations
This demo builds the image locally. It does not push to Docker Hub or deploy to cloud/Kubernetes. The Jenkins agent must be Linux-based for the shell commands as written. Never commit passwords or tokens. For a production extension, add secret-managed registry credentials, image scanning, HTTPS, monitoring, and a deployment target.

## Interview explanation
"I developed a Flask application and implemented a Jenkins declarative CI/CD pipeline. When code is pushed to GitHub, Jenkins checks out the source, runs pytest tests in an isolated Python container, builds a Docker image, starts the container, and validates its health endpoint. The image uses Gunicorn, a non-root user, and a Docker health check."

## Resume entry
**Automated CI/CD Pipeline for a Containerized Flask Application**
- Developed a Python Flask application with health and application-info REST endpoints.
- Configured a Jenkins declarative pipeline to automate source checkout, pytest execution, Docker image creation, and container smoke testing.
- Containerized the application using Docker and provided Docker Compose configuration for repeatable local deployment.
