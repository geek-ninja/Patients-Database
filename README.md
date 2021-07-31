[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Patients-Database

<h2>Patient Datababe Website made using Django</h2><br>
<p>Here you can upload data of the patient and update the data and delete and view of details of the patients</p>

<p>hope you have installed django or else you can follow the command</p><br>
python -m pip install Django
<br>
<h3>Create the project</h3>
django-admin startproject hospital
<br>
<p>change the directory to the new project folder created</p>
<p>Then create the app for the project</p>
python3 manage.py startapp patient
<br>
<br>
<p>For quick overview of the project you can copy and overwrite the files and folder from the repo to the respective files of django that you have created</p>
<h3>How to run the django server</h3>
<p>now run the following commands</p>
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py runserver

