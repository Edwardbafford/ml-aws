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
  
  // Push Chart to Helm Repo
  stage('Helm') {
    sh 'helm package ./helm/ml-aws/'
    sh 'helm push ./helm/ml-aws/ chartmuseum'
  }
  
  // Clean and prepare environment after changes have been made
  stage('Clean') {
    sh 'helm repo update chartmuseum'
    sh 'docker system prune -f'
  }
}
