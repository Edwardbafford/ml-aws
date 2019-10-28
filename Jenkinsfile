node {
  // Setup
  sh 'git -C /home/lbafford_mprove/ml-aws pull origin master'
  def controllerImage
  def cnnImage
  
  // Build and test controller service
  stage('Controller') {
    controllerImage = docker.build("edwardbafford/ml-controller:latest", "/home/lbafford_mprove/ml-aws/Services/controller")
  }
  
  // Build and test CNN service
  stage('CNN') {
    cnnImage = docker.build("edwardbafford/ml-cnn:latest", "/home/lbafford_mprove/ml-aws/Services/cnn")
  }
  
  // Push built images to dockerhub repository
  stage('Push') {
    docker.withRegistry('https://index.docker.io/v1/', 'docker') {
      controllerImage.push()
      cnnImage.push()
    }
  }
  
  // Re-package chart and push to chartmuseum repo
  stage('Helm') {
    sh 'helm push /home/lbafford_mprove/ml-aws/helm/ml-aws chartmuseum'
  }  
  
  // Clean and prepare environment after changes have been made
  stage('Clean') {
    sh 'helm repo update chartmuseum'
    sh 'docker system prune -f'
  }
}
