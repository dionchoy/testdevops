# Instructions to 

Install minikube
```
minikube start
kubectl apply -f deploy.yml
kubectl apply -f svc.yml
kubectl port-forward --address 0.0.0.0 svc/testlib-svc 5000:5000
```