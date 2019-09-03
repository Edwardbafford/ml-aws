pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                docker.build('ml-aws')
            }
        }
        stage('Push') {
            steps {
                docker.withRegistry('https://403644602806.dkr.ecr.us-west-2.amazonaws.com', 'ecr:us-west-2:ml-aws') {
                    docker.image('ml-aws').push('latest')
                }
            }
        }
    }
}
