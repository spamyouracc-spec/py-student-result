pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
               
                git branch: 'main', url: ' https://github.com/<your-github-username>/<your-repo-name>.git&#x27 ;
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
