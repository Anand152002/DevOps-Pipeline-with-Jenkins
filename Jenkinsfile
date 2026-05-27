pipeline {

    agent any

    stages {

        stage('Build Docker Image') {

            steps {
                sh 'docker build -t talentsync .'
            }
        }

        stage('Run Tests') {

            steps {
                sh 'pytest'
            }
        }

        stage('Deploy Container') {

            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
