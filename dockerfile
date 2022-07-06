#buster -> stable Debian release is 10.4, and its codename is “Buster.”
#slim   -> This image generally only installs the minimal packages needed

FROM python:3.8-slim-buster



# Set working directory to app
WORKDIR /app 

#Install dependencies

#Copy the requirements.txt file to the app directory
COPY requirements.txt requirements.txt

#Install the requirements
RUN pip3 install -r requirements.txt

#copy all files to the app directory
COPY . .

# FLASK_APP environment variable is used to specify how to load the application
RUN export FLASK_APP=app.py

# run the app
# --host=0.0.0.0 -> This tells your operating system to listen on all public IPs.
# -m module-name -> Searches sys.path for the named module and runs the corresponding .py file as a script.
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]