# kube-project
a kuberntes docker project 


build docker using 'docker build -t api-fetch-service .'
(or without docker using 'uvicorn app.main:app --reload')
start server using 'docker run --env-file .env -p 8000:8000 api-fetch-service'


# start server using uvicorn app.main:app --reload
get data using     'curl http://127.0.0.1:8000/data'
check health using 'curl http://127.0.0.1:8000/health'
