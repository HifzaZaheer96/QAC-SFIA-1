pipeline {
    agent any
    stages {
        stage('Development Environment') {
            steps {
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh './script/make_service.sh'
            }
        }

         stage('Testing'){
            steps {
                sh 'coverage run -m pytest test/testing.py'
                sh 'coverage report'
            }
         }
    }
}

