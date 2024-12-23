pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Клонируем репозиторий с вашим проектом
                
             git branch: 'main', url: 'git@github.com:khodalex/testcalj.git'

            }
        }

        stage('Build Docker Image') {
            steps {
                // Собираем Docker-образ
                script {
                    docker.build('python-calculator')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                // Запускаем Docker-контейнер
                script {
                    docker.image('python-calculator').inside {
                        sh 'python calculatorj.py'
                    }
                }
            }
        }
    }
}
