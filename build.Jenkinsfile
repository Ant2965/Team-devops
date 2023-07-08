pipeline {
    agent any

    environment {
        ECR_URL = '854171615125.dkr.ecr.us-east-1.amazonaws.com'
        REPO_NAME = 'system-monitorteamdev'
    }

    stages {
        stage('ECR authentication and Docker login') {
            steps {

                sh '''
                aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 854171615125.dkr.ecr.us-east-1.amazonaws.com
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                
                docker build -t ${REPO_NAME} .
                '''
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                docker tag ${REPO_NAME} ${ECR_URL}/${REPO_NAME}:0.0.${BUILD_NUMBER}
                docker push ${ECR_URL}/${REPO_NAME}:0.0.${BUILD_NUMBER}
                '''
            }
        }
    }
}