pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully.'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Python environment...'
                // هنستخدم python أو python3 المتاح، وبنحط --break-system-packages عشان لو الـเวอร์ชั่น جديدة في دبيان/أوبونتو متعملش بلوك
                sh 'pip install --no-cache-dir -r requirements.txt --break-system-packages || pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                // تشغيل التست علطول بـ python -m pytest أو pytest
                sh 'python3 -m pytest test_app.py || python -m pytest test_app.py || pytest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                // تشغيل التطبيق في الخلفية
                sh 'nohup python3 app.py > flask.log 2>&1 & || nohup python app.py > flask.log 2>&1 &'
                echo 'Application deployed and running.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}