pipeline {
    agent any
    environment {
        IMAGE_NAME = "flask-devops-cicd"
        CONTAINER_NAME = "flask-devops-ci-test"
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Install and Test') {
            steps {
                sh '''
                    docker run --rm -v "$WORKSPACE:/workspace" -w /workspace python:3.12-slim sh -c "pip install --no-cache-dir -r requirements.txt && pytest -q"
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
                sh 'docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest'
            }
        }
        stage('Container Smoke Test') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} ${IMAGE_NAME}:${BUILD_NUMBER}
                    sleep 5
                    docker run --rm --network container:${CONTAINER_NAME} curlimages/curl:8.10.1 -fsS http://127.0.0.1:5000/health
                '''
            }
        }
    }
    post {
        always {
            sh 'docker rm -f ${CONTAINER_NAME} || true'
            cleanWs()
        }
        success { echo 'CI/CD pipeline completed successfully.' }
        failure { echo 'Pipeline failed. Check the stage logs.' }
    }
}
