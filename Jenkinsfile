pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
               
                git branch: 'main', url: 'https://github.com/spamyouracc-spec/py-student-result.git'
            }
        }
        stage('Build and Run') {
            steps {
                script {
                    bat 'python calculator.py'
                }
            }
        }
    }
}
