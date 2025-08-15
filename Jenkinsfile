pipeline {
    agent any
    environment {
        DOCKERHUB_USER = 'darshancr9'
        IMAGE = "${DOCKERHUB_USER}/flask-hello"
        APP_PORT = "8000" // inside container
        HOST_PORT = "8081" // on EC2 host
        CONTAINER_NAME = "flask-hello"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker image') {
            steps {
                sh 'docker build -t $IMAGE:$BUILD_NUMBER .'
            }
        }
        stage('Tag & Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    sh '''
                        echo "$PASS" | docker login -u "$USER" --password-stdin
                        docker tag $IMAGE:$BUILD_NUMBER $IMAGE:latest
                        docker push $IMAGE:$BUILD_NUMBER
                        docker push $IMAGE:latest
                    '''
                }
            }
        }
        stage('Run Container') {
            steps {
                sh '''
                    docker rm -f $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME -p ${HOST_PORT}:${APP_PORT} $IMAGE:latest
                    docker ps
                '''
            }
        }
    }
    post {
        always {
            sh 'docker logout || true'
        }
    }
}
