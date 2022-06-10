# REST-ful API design with Flask
To run this program, you need to install the dependencies related to the program so that you can run the program. All the necessary libraries are placed in the ```requirements.txt``` file. You can install them one by one with the command ```pip install``` or install all the libraries together with the following command:
```
$ pip install -r requirements.txt
```
After installing the libraries, you can run the program with the following command:
```
$ flask run
```
When you run this program for the first time, it creates a database for you. After creating the database, stop the program and delete or comment on following code:
```py
db.create_all()
```
in the program code so that it does not rebuild the database again in the next executions.

Run the program again. Now you can work with this API. I put the ```test.py``` file for you and wrote a small test of my own in it. At the same time as running the main code, you can run this test file to see this API It works or not. You can also delete my tests and put your own tests.

To run the test, you must enter the following command:
```
$ python3 test.py
```

**Note that the test file must be executed when the API code is running. If you run this code when the main program code is not running, you will receive an error**