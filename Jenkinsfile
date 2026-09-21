pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python --version'
            }
        }

       stage('Test') {
    steps {
        bat 'python -m pip install pytest'
        bat 'python -m pytest tests'
    }
}
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}