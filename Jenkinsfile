pipeline {
    agent any

    stages {
        stage('Setup Python Environment') {
    steps {
        bat '"C:\\Program Files\\Python310\\python.exe" -m pip install -r requirements.txt'
    }
}


        stage('Extract Data') {
            steps {
                bat '"C:\\Program Files\\Python310\\python.exe" extract.py'
            }
        }
    }
}
