pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // هتقوم بسحب الكود تلقائيًا من ريبو GitHub اللي مربوط بالـ Job
                checkout scm
                echo 'Source code checked out successfully.'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Python environment...'
                // تجهيز البيئة وتسطيب المكتبات
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                // تشغيل ملف التست اللي عملناه
                sh './venv/bin/pytest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                // تشغيل التطبيق في الخلفية (Background) عشان يفضل قايم ونشوف الـ UI
                // ملاحظة: تم استخدام PORT 5000
                sh 'nohup ./venv/bin/python app.py > flask.log 2>&1 &'
                echo 'Application deployed and running on http://localhost:5000'
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