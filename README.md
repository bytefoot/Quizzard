# Quizzard
A quizzing web application which randomly generates and gives a set of 10 questions based
on the topic chose by the user.

It also maintain a history of all the quizes attempted by the user along with the marks in
that quiz.

## Setup and Execution Instructions
Note: It best works with python version >= 3.9

1. Create a venv using:
    ```python3 -m venv venv```

2. Activate the environment:
    - Mac\Linux
        ```source ./venv/bin/activate``` 
    - Windows
        ```.\venv\Scripts\activate.bat```

3. Install the the require dependancies from 'requirements.txt'
    ```pip install -r requirements.txt```

4. Make sure the database is created and reloaded. To do that, after opening terminal in the parent directory
    run
        ```flask shell```
    which spins up a python IDLE in the terminal. In the IDLE:
        ```from app import db
        db.drop_all()
        db.create_all()
        exit()```

5. Now that everything is setup, the application can finally be run. Make sure, you are still located inside
    the parent directoy run the app using:
    ```flask run```
    This would spawn up a local server which can be utilised to test the application.

## Link to demo of the web application
[The vid :sparkles:](https://drive.google.com/file/d/1Qb1-KG5JAIfyNzD5YihVSn-hGJsLgoLS/view?usp=sharing).