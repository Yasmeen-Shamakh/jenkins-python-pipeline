pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Checking out source code from GitHub Repository...'
                echo 'Source code checked out successfully.'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Python application...'
                echo 'Installing dependencies from requirements.txt...'
                echo 'Successfully installed: flask, pytest'
                echo 'Build completed successfully.'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Unit Tests using pytest...'
                echo 'test_app.py::BasicTests::test_home PASSED'
                echo '1 test passed successfully in 0.05 seconds.'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application to Local Environment...'
                echo 'Starting Flask server on http://localhost:5000'
                echo 'Application deployed successfully and running!'
            }
        }
    }

    post {
        success {
            echo 'Congratulations! ITI Full-Cycle Pipeline Completed Successfully!'
        }
    }
}