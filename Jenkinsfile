pipeline{
    agent any{
        environments{
            VENV='myenv'

        }
        stages{
            stages('Chekcout Out'){
                steps{
                    git branch: 'master',url: 'https://github.com/imranworkspace/Jenkins'
                }
            }
        }
        stage('SET up myenv'){
            steps{
                bat 'python -m venv %myenv%'
                bat '%myenv%\\Scripts\\python -m pip install --upgrate pip'
                bat '%myenv%\\Scripts\\pip install -r '
            }
        }
    }
    stage('run the tests'){
        steps{
            bat '%myenv%\\Scripts\python manage.py test myapp.tests.test_views'
        }
    }
}