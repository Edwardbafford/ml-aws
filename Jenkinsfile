node {
  checkout scm
  def controllerImage
  def cnnImage
  
  stage('Controller') {
    controllerImage = docker.build("edwardbafford/ml-controller:latest", "./Services/controller")
  }
  
  stage('CNN') {
    cnnImage = docker.build("edwardbafford/ml-cnn:latest", "./Services/cnn")
  }
  
  stage('Push') {
    docker.withRegistry('https://index.docker.io/v1/', 'docker') {
      controllerImage.push()
      cnnImage.push()
    }
  }
}
