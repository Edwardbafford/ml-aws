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
  
  // Push built images to dockerhub repository
  stage('Push') {
    docker.withRegistry('https://index.docker.io/v1/', 'docker') {
      controllerImage.push()
      cnnImage.push()
    }
  }
  
  // Refresh k8s pods
  stage('k8s') {
    sh 'kubectl rollout restart deployment/cnn-deployment'
    sh 'kubectl rollout restart deployment/controller-deployment'
  }
  
  // Clean and prepare environment after changes have been made
  stage('Clean') {
    sh 'docker system prune -f'
  }
}
