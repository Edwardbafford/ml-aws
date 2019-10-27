node {
  checkout scm
  def controllerImage
  
  stage('Controller') {
    controllerImage = docker.build("edwardbafford/ml-controller:latest", "./Services/controller")
  }

  stage('Push images') {
    docker.withRegistry('https://index.docker.io/v1/', 'docker') {
      controllerImage.push()
    }
  }
}
