pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
               withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'aws_creds', usernameVariable: 'PUBLIC', passwordVariable: 'PRIVATE']]) {
                   sh 'docker build --tag=ml-aws --build-arg public_key=$PUBLIC  --build-arg private_key=$PRIVATE .'
               }
            }
        }
        stage('Push') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
