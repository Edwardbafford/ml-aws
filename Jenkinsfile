node {
  // Setup
  checkout scm
  def controllerImage
  def cnnImage
  
  // Build and test controller service
  stage('Controller') {
    controllerImage = docker.build("edwardbafford/ml-controller:latest", "./Services/controller")
  }
  
  // Build and test CNN service
  stage('CNN') {
    cnnImage = docker.build("edwardbafford/ml-cnn:latest", "./Services/cnn")
  }
  
  // Push built images
  stage('Push') {
    docker.withRegistry('https://index.docker.io/v1/', 'docker') {
      controllerImage.push()
      cnnImage.push()
    }
  }
}
