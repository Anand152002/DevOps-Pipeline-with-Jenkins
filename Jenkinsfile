pipeline {

    agent any

    stages {

        stage('Build Docker Image') {

            steps {
                bat 'docker build -t talentsync .'
            }
        }

        stage('Run Tests') {

            steps {
                bat 'pytest'
            }
        }

        stage('Deploy Container') {

            steps {
                bat 'docker-compose up -d'
            }
        }
    }
}