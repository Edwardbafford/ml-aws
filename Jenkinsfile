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
                sh 'pwd'
                sh 'git --version'
                sh 'docker ps'
            }
        }      
    }
}
