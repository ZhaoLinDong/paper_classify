pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Setup') {
            steps {
                bat '''
                    python -m venv .venv
                    .venv\\Scripts\\python.exe -m pip install -U pip
                    .venv\\Scripts\\pip.exe install -r requirements.txt
                '''
            }
        }

        stage('Check') {
            steps {
                bat '''
                    .venv\\Scripts\\python.exe -m py_compile paper_classify.py
                '''
            }
        }
    }
}
