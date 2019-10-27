node {
  checkout scm

  stage('Controller') {
    def controllerImage = docker.build("edwardbafford/ml-controller")
  }

  stage('Push images') {
    docker.withRegistry('https://index.docker.io/v1/', 'ZWR3YXJkYmFmZm9yZDpTdXBlcmdva3UxIQ==') {
      controllerImage.push()
    }
  }
}
