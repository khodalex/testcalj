pipeline {
    agent any

    environment {
        OPERATION = 'add'  // Операция по умолчанию
        NUM1 = '10'        // Первое число
        NUM2 = '5'         // Второе число
        DOCKER_IMAGE = 'python-calculator'
        REMOTE_SERVER = 'mamange@10.0.0.130'  // Адрес вашего сервера
        PROJECT_DIR = '/home/manage/project'   // Путь к директории на сервере
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
                    // Строим Docker-образ на Jenkins
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Копируем проект и Dockerfile на сервер, собираем образ и запускаем контейнер
                    sshagent(['8eb21d70-c6e9-4779-8c7d-79d98aafd274']) {
                        sh '''
                        # Копируем проект на сервер
                        scp -r . ${REMOTE_SERVER}:${PROJECT_DIR}

                        # На сервере строим Docker-образ и запускаем контейнер с нужными параметрами
                        ssh ${REMOTE_SERVER} "
                        cd ${PROJECT_DIR} && \
                        docker build -t ${DOCKER_IMAGE} . && \
                        docker run --rm ${DOCKER_IMAGE} ${OPERATION} ${NUM1} ${NUM2}"
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
        always {
            cleanWs()  // Очищаем рабочее пространство после выполнения
        }
    }
}
