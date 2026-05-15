pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully.'
            }
        }

        stage('Install System Python') {
            steps {
                echo 'Updating system and installing Python3 & Pip inside Jenkins...'
                sh 'sudo apt-get update && sudo apt-get install -y python3 python3-pip python3-venv || apt-get update && apt-get install -y python3 python3-pip python3-venv'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Virtual Environment & Installing Dependencies...'
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running Real Unit Tests...'
                sh './venv/bin/pytest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                sh 'nohup ./venv/bin/python app.py > flask.log 2>&1 &'
                echo 'Application is running inside Jenkins Container.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
    }
}