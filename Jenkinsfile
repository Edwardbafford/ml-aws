node {
    checkout scm
    def controllerImage = docker.build("edwardbafford/ml-controller", "./Services/controller")
    controllerImage.push('latest')
}
