# dockerfile - blueprint for creating an image

FROM python:3.9
ADD main.py .

# RUN pip install -r requirements.txt
# cmd line arguments that pass the mac accress via the docker file to retrieve the json payload response

CMD ["python3", "main.py", "44:38:39:ff:ef:57"]
# image -  template for running the container

# container - is running the python program inside it