# kube-project
a kuberntes docker project 


build docker using 'docker build -t api-fetch-service .'
(or without docker using 'uvicorn app.main:app --reload')
start server using 'docker run --env-file .env -p 8000:8000 api-fetch-service'


# start server using uvicorn app.main:app --reload
get data using     'curl http://127.0.0.1:8000/data'
check health using 'curl http://127.0.0.1:8000/health'


# do run in kubernetes do:
minikube start
minikube image load api-fetch-service
kubectl apply -f ./yamls/
minikube service api-fetch-service --url

It should give you the curl call 
somehthing like http://127.0.0.1:53509/data


# Using Helm
run first time do 
cd api-fetch-service
helm upgrade --install api-fetch-service .
