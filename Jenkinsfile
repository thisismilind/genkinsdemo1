pipeline {
    agent any
    stages {
        stage('checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Extract Data') {
            steps{
                bat "C:\\Program Files\\Python310\\python.exe extract.py"

            }
        }
    }
}