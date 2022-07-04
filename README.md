# LITReview
##

## Features

- Python v3.x+
- [Django](https://www.djangoproject.com/)
- [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)
  This ensures you'll be able to install the correct packages without interfering with Python on your machine.
  Before you begin, please ensure you have this installed globally. 


## Installation

 - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.
 - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>
- Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>
- then go to the LITReview folder
- You should now be ready to start the application. In the directory, type either <code>python manage.py runserver</code>.
-now you can go to the app  by typing <code>127.0.0.1:8000</code> in your favorite browser .

## linner

this projest use [flake8](https://flake8.pycqa.org/en/latest/) as linner

- To run the linner do <code>flake8</code> in the LITreview directory 
