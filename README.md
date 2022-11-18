to build a rest api docker

1. mkdir docker_folder

2. cd docker_folder

3. wget https://raw.githubusercontent.com/jingyanwang/flusk_utility/master/Dockerfile

4. docker build -t docker_template .

5. docker run -it -p 0.0.0.0:3941:3941 91ff1deb9a73

6. go to web explorer and open http://0.0.0.0:3941/
