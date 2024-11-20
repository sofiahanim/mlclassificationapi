# mlclassificationapi
Deploy a trained ML model into a Docker container and create an API. 

Ez pz steps:

1. Download os python version. Each line in Dockerfile is executed.
```
docker build -t image_name .
```
2. Create container. (note: if container_name is already exist, delete them or use other name)
```
docker run --name container_name -p 8000:8000 image_name
```
3. Check uvicorn running on http://0.0.0.0:8000
Note: Otherwise, try below address
```
http://localhost:8000
```
```
http://127.0.0.1:8000
```
If u see like below, u are good to go

![image](https://github.com/user-attachments/assets/e7f084aa-3299-47a2-b91a-713f0e795aa1)

4. Next, check on docs at  http://0.0.0.0:8000/docs to explore and test
   ![image](https://github.com/user-attachments/assets/2bb37462-1e7e-4b55-8a03-5e355e5cf1c2)


6. Try inside postman too
   ![image](https://github.com/user-attachments/assets/78216278-445c-43fb-8f82-904dcde9b212)



Voila! kk bye
