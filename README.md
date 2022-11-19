to build a rest api docker

1. mkdir docker_folder

2. cd docker_folder

3. wget https://raw.githubusercontent.com/jingyanwang/flusk_utility/master/Dockerfile

4. 

```bash
docker build -t flask_swagger:1.0.1 .
```

5. 

```bash
docker run -it -p 0.0.0.0:3941:3941 flask_swagger:1.0.1
```

6. go to web explorer and open http://0.0.0.0:3941/
