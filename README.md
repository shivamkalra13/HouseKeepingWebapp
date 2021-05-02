# HouseKeepingWebapp
It is a Python Django based webapp

### Frontend:-
##### ->HTML5
##### ->CSS3
##### ->Javascript
##### ->Bootstrap4

### Backend :-
##### ->DJango(Python)

### For running this app:-
* first configure your pc by installing python packages mentioned requirements.txt(in the project's directory) and set environment variables for python.
* After installing all the packages, open CMD and move to the project directory and run the command "python manage.py runserver".
* (sometimes before this command you may need to run :-
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser{this command will create a new admin account for webapp})
* Then open localhost/first_app/index(localhost address will show up in CMD after running above commands)

### Following urls are important:-
* localhost/first_app/index - It is the home page of webapp
* localhost/first_app/add-asset/ - API 1
* localhost/first_app/add-task/ - API 2
* localhost/first_app/add-worker/ - API 3
* localhost/first_app/assets/all/ - API 4
* localhost/first_app/allocate-task/ - API 5
* localhost/first_app/get-tasks-for-worker/{workerid} - API 6    =>example->http://127.0.0.1:8000/first_app/get-tasks-for-worker/w1

* Rest urls can be reached from home page.

### Some screenshots of the app: -
![Capture1](https://github.com/shivamkalra13/HouseKeepingWebapp/blob/master/Capture1.JPG)

![Capture2](https://github.com/shivamkalra13/HouseKeepingWebapp/blob/master/Capture2.JPG)

![Capture3](https://github.com/shivamkalra13/HouseKeepingWebapp/blob/master/Capture3.JPG)

![Capture4](https://github.com/shivamkalra13/HouseKeepingWebapp/blob/master/Capture4.JPG)
