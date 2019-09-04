pipeline {
    agent any
    stages {
        stage('Clean') {
            steps {
                sh 'docker container stop ml-aws || true'
                sh 'docker system prune -f'
            }
        }      
        stage('Build') {
            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'aws-creds-2', usernameVariable: 'PUBLIC', passwordVariable: 'PRIVATE']]) {
                   sh 'docker build --tag=ml-aws --build-arg public_key=$PUBLIC --build-arg private_key=$PRIVATE .'
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://403644602806.dkr.ecr.us-west-2.amazonaws.com', 'ecr:us-west-2:ml-aws') {
                        docker.image('ml-aws').push('latest')
                    }
                }
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -p 8000:80 --name ml-aws  403644602806.dkr.ecr.us-west-2.amazonaws.com/ml-aws'
            }
        }
    }
}
