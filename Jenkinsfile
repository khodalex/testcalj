pipeline {
    agent any

    environment {
        OPERATION = 'add'  // Устанавливаем операцию
        NUM1 = '10'        // Устанавливаем первое число
        NUM2 = '5'         // Устанавливаем второе число
    }

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
                // Запускаем Docker-контейнер с передачей переменных окружения для выполнения операции
                script {
                    docker.image('python-calculator').inside {
                        sh """
                            python calculatorj.py ${OPERATION} ${NUM1} ${NUM2}
                        """
                    }
                }
            }
        }
    }
}
