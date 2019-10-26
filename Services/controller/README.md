Controller Micro Service used for coordinating between different Machine Learning components. This service provides the only front aspect of the application.  
  
## DOCKER  
docker build --tag=ml-controller .  
docker run -d --rm -p 8080:80 ml-controller  
  
## K8S  
kubectl apply -f .\controller-deployment.yaml  
kubectl expose deployment controller-deployment --type=LoadBalancer --name=controller-service  
Use external ip of service to access application at port 80