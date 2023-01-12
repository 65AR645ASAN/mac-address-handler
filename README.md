# MAC-ADDRESS API-HANDLER 
- Importent Note - The Requirements.txt File is a sample, its presence is semantic and extensible if external libraries if they need to be leveraged in the future
- Please follow the following instructions to successfully execute this main.py script in the
    - Install python3 on your computer from python.org {https://www.python.org/downloads/}
    - Install docker on your computer from {https://www.docker.com/products/docker-desktop/}
    - Run the following commands to execute the main.py script
        - It can be run directly using the following command
        - python3 main.py [macaddress]
        > python3 main.py 44:38:39:ff:ef:57
        
    - It can be run via a DockerFile with the following commands after docker desktop is available on your computer 
        > docker run -d -p 80:80 docker/getting-started
        - Next create a docker image with the Dockerfile
            - docker build -t [image-name] .
            > docker build -t mainimage .
            - Running the mainimage runs the cmds in the dockerfile exectuing the main.py script that logs the company name requested from the output
            > docker run mainimage 
- SECURITY - Can be added to making the api key a parameter that is passed to the script along with the mac address, [currently its hardcoded] the class and function is written to add this as a security parameter