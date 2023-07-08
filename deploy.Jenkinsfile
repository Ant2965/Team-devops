pipeline {
    agent any

    environment {
        ECR_URL = '854171615125.dkr.ecr.us-east-1.amazonaws.com'
        REPO_NAME = 'system-monitorteamdev'
    }

    stages {
        stage('Deploy') {
            steps {

                sh '''
                aws eks --region us-east-2 update-kubeconfig --name k8s-batch1
                python3 eks.py
                
                '''
            }
        }
    }
}