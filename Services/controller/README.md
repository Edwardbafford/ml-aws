Controller Micro Service used for coordinating between different Machine Learning components. This service provides the only front aspect of the application.  
  
docker build --tag=ml-controller .  
docker run -d --rm -p 8080:80 ml-controller