# mac address handler 
- importent note - the requirements.txt file is a sample, if the script is to be extended to support from external libraries
- install python3 on your computer from python.org {https://www.python.org/downloads/}
- install docker on your computer from {https://www.docker.com/products/docker-desktop/}
- run the following commands to execute the main.py script
    - it can be run directly using the following command
        - python3 main.py [macaddress]
        > python3 main.py 44:38:39:ff:ef:57
        
    - it can be run via a DockerFile with the following commands afrter docker desktop is available on your computer 
        > docker run -d -p 80:80 docker/getting-started
        - next create a docker image with the Dockerfile
            - docker build -t [image-name] .
            > docker build -t mainimage .
            > docker run mainimage
