node {
    checkout scm
    sh 'docker login --username=edwardbafford'
    
    def controllerImage = docker.build("edwardbafford/ml-controller", "./Services/controller")
    controllerImage.push('latest')
}
