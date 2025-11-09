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
                bat "C:\\Users\\milind\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe extract.py"

            }
        }
    }
}