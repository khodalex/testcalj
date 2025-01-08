pipeline {
    agent any

    environment {
        OPERATION = 'add'  // Операция по умолчанию
        NUM1 = '10'        // Первое число
        NUM2 = '5'         // Второе число
        DOCKER_IMAGE = 'python-calculator'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Клонируем репозиторий
                git branch: 'main', url: 'git@github.com:khodalex/testcalj.git'
            }
        }

   

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Копируем Dockerfile и проект на сервер, собираем и запускаем контейнер
                    sshagent(['8eb21d70-c6e9-4779-8c7d-79d98aafd274']) {
                        sh '''
                        scp -r . mamange@10.0.0.130:/home/user/project
                        ssh mamange@10.0.0.130 "cd /home/user/project && \
                        docker build -t ${DOCKER_IMAGE} . && \
                        docker run --rm ${DOCKER_IMAGE} ${OPERATION} ${NUM1} ${NUM2}"
                        '''
                    }
                }
            }
        }
    }
}
