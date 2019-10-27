node {
    checkout scm
    sh 'docker login'
    
    def controllerImage = docker.build("edwardbafford/ml-controller", "./Services/controller")
    controllerImage.push('latest')
}
