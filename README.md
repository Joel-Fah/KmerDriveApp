# tppoo
Implementing an object-oriented solution using Python to an urban trasnport problem

## Problem Description
On the other hand, Urban transport in many African countries in general and in Yaounde in particular is now well known. In effect, the expansion of cities such as Yaounde is accompanied by territorial growth as the population occupies more spaces. Thus, distances are continually increasing between residents and their work place. By consequence, there is an increase in the use of existing facilities, and a greater number of trips. The development of urban transport and the improvement in public services, particularly passenger transport, influences the population time and budget. The complex of various types of transportation of people in Yaounde and the difficulties to identify and well describe the place to go make things more worse for newcomers in the town and sometimes for people living there. The second exercise of this practice involves the development of a solution to help the general public to get more easily access to passenger transport. This is the mass public transport carrying passengers along predetermined routes subdivided into streets (taxi, motor bus, private motor vehicles, bus, etc.). Thus, to build an interface using a map to guide a user to identify the place to go given the current place.

## Objective: 
The main goal of the overall practice exercise is to allow the students to understand how to analyze and design applications using Object Oriented Techniques. On the other hand, they will learn how to implement software using Object Oriented Programming techniques. Thus, firstly, the students will collect data on some of their daily activities. Thereafter, they will use this data to design and develop an application.

## Installation & Launching
Our application is running on django version 4.0.4
To install, follow the following steps:
Place yourself at the root of the project.
(Linux) /home/.../KmerDrive/

Setup the virtual environment for the project at its root by running the following commands:
Install pip first: sudo apt-get install python3-pip.
Then install virtualenv using python3-venv: sudo apt-get install python3-venv
Now create a virtual environment: python3 -m venv venv (you can use any name instead of venv)

Activate your virtual environment on Linux: source ./venv/bin/activate

To deactivate the already activated virtual environment, simply type deactivate in the terminal.

Inside the created and activated virtual environment, Install the required packages from requirements.txt by running the command: pip install -r requirements.txt

Launching of the project
Before executing the following commands, always make sure you are at the root of the project.
Migrate the data to the database (db.sqlite3 by default):  python manage.py migrate

Run the project using the command: python3 manage.py runserver

Check the server is running by going to http://127.0.0.1:8000
