# MAC-ADDRESS API-HANDLER 
- Importent Note - The Requirements.txt File is a sample, if the script is to be extended to support from external libraries
- Install python3 on your computer from python.org {https://www.python.org/downloads/}
- Install docker on your computer from {https://www.docker.com/products/docker-desktop/}
- Run the following commands to execute the main.py script
    - It can be run directly using the following command
        - python3 main.py [macaddress]
        > python3 main.py 44:38:39:ff:ef:57
        
    - It can be run via a DockerFile with the following commands afrter docker desktop is available on your computer 
        > docker run -d -p 80:80 docker/getting-started
        - Next create a docker image with the Dockerfile
            - docker build -t [image-name] .
            > docker build -t mainimage .
            > docker run mainimage
