pipeline {
    agent any

    environment {
        ECR_URL = '854171615125.dkr.ecr.us-east-1.amazonaws.com'
        REPO_NAME = 'system-monitorteamdev'
    }
    parameters { string(name: 'CPU_IMAGE', defaultValue: '', description: '') }
    //commented
    stages {
        stage('Deploy') {
            steps {

                sh '''
                sed -i "s%CPUIMAGE%$CPU_IMAGE%g" deploy.yaml
                aws eks --region us-east-2 update-kubeconfig --name k8s-batch1
                kubectl apply -f deploy.yaml
                
                '''
            }
        }
    }
}