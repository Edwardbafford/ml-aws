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
                sh 'docker build --tag=edwardbafford/ml-controller /home/lbafford_mprove/ml-aws/Services/controller/'
                sh 'docker push edwardbafford/ml-controller'
            }
        }
        stage('CNN') {
            steps {
                sh 'docker build --tag=edwardbafford/ml-cnn /home/lbafford_mprove/ml-aws/Services/cnn/'
                sh 'docker push edwardbafford/ml-cnn'
            }
        } 
    }
}
