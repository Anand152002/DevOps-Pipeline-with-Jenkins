pipeline {
    agent any

    environment {
        IMAGE_NAME = 'talentsync'
        CONTAINER_NAME = 'talentsync_container'
    }

    stages {

        stage('Build') {
            steps {
                echo 'Building Docker Image'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Pytest'
                sh 'pytest --maxfail=1 --disable-warnings -v'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Running SonarQube Analysis'
                sh 'sonar-scanner'
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Running Bandit Security Scan'
                sh 'bandit -r app/'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Container'
                sh 'docker-compose down || true'
                sh 'docker-compose up -d'
            }
        }

        stage('Release') {
            steps {
                echo 'Creating Release Tag'
                sh 'git tag v1.${BUILD_NUMBER}'
            }
        }

        stage('Monitoring') {
            steps {
                echo 'Checking Application Health'
                sh 'curl http://localhost:8000/'
            }
        }
    }
}
