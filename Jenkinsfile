node {
  checkout scm

  stage('Controller') {
    def controllerImage = docker.build("edwardbafford/ml-controller", "./Services/controller")
  }

  stage('Push images') {
    docker.withRegistry('https://index.docker.io/v1/', 'docker') {
      controllerImage.push()
    }
  }
}
