pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -U pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Check') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python3 -m py_compile paper_classify.py
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
