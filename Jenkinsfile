pipeline {
    agent any
    stages {
        stage('Clean') {
            steps {
                sh 'cd /home/lbafford_mprove/ml-aws'
                sh 'git pull origin master'
            }
        }  
        stage('Controller') {
            steps {
                sh 'cd /home/lbafford_mprove/ml-aws/Services/controller/'
                sh 'docker build --tag=edwardbafford/ml-controller .'
                sh 'docker push edwardbafford/ml-controller'
            }
        }
        stage('CNN') {
            steps {
                sh 'cd /home/lbafford_mprove/ml-aws/Services/cnn/'
                sh 'docker build --tag=edwardbafford/ml-cnn .'
                sh 'docker push edwardbafford/ml-cnn'
            }
        } 
    }
}
