# ml-aws
Small Machine Learning application deployed on Google's cloud platform and leverages their K8s cluster service. In using K8s the system is divided into micro-services. Each directory within the services folder contains an independently deployable application. The intention of this project is to display my abilities to skills in software engineering as well as my understanding of Machine Learning.  
  
## Controller
The only front end component of the system and is used to coordinate between the various machine learning services.  
  
## CNN
Image processing service used to dynamically predict the type of flower from a JPG (only!) image. This service is provided by retraining a google developed CNN.
