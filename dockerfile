FROM python:3.8-slim-buster

# set working directory to app
WORKDIR /app 

#install dependencies
#copy the requirements.txt file to the app directory
COPY requirements.txt requirements.txt

# install the requirements
RUN pip3 install -r requirements.txt

#copy all files to the app directory
COPY . .

RUN export FLASK_APP=app.py

# run the app
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]