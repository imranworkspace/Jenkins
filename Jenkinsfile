pipeline {
    agent any

    environment {
        VENV = "myenv"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/imranworkspace/Jenkins'
            }
        }

        stage('Setup Virtualenv') {
            steps {
                bat "python -m venv %VENV%"
                bat "%VENV%\\Scripts\\python -m pip install --upgrade pip"
                bat "%VENV%\\Scripts\\pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat "%VENV%\\Scripts\\python manage.py test myapp.tests.test_views"
            }
        }
    }
}
