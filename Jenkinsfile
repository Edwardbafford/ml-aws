pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
               withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'aws_creds', usernameVariable: 'PUBLIC', passwordVariable: 'PRIVATE']]) {
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
