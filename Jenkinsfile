pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
               withCredentials([[credentialsId: 'aws_creds', usernameVariable: 'PUBLIC', passwordVariable: 'PRIVATE']]) {
                   sh 'echo uname=$PUBLIC pwd=$PRIVATE'
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
