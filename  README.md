#### Casting Agency:
Thesis:
  This project will allow users to view/delete/add/update actor and movie data using their specific roles. This project contains main part of third party services like Auth0 for authentication, using postgres for database and heroku for deployment 

#### Virtual Enviornment

Using virtual environment for Python project. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### pip Dependencies

* Installing Dependencies
  For a Python application, Heroku looks for a requirements.txt file that needs to include all of your dependencies.Once you have your virtual environment setup and running, install dependencies : `pip freeze > requirements.txt`

* Key Dependencies
  - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

  - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM, let's handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

  - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension, let's handle cross origin requests from our frontend server. 


## Running the server

  With in the directory first ensure you are working using your created virtual environment.
  To run the server, execute:
    `export FLASK_APP=app.py` 
    `flask run --reload`

#### Auth0 services 

  Create an account in [Auth0] https://auth0.com/ and create an aplication and set api. Later assigne role to each users which they have permission gives to acces limited data.

# Getting Started on Heroku

Download Heroku:
  First create an account with Heroku here and then we need to download the Heroku CLI (Command Line Interface) in order to run commands from the terminal that enable us to create a Heroku application and manage it.

  After you create your account, install Heroku with Homebrew by running: `brew tap heroku/brew && brew install heroku`
  To see location of file use: `which heroku`

# Deployment Configuration:

 * Environment Configuration
    Use `touch setup.sh` and set up all of the environment variables in that file.

 * Gunicorn
    Gunicorn is a pure-Python HTTP server for WSGI applications. We'll be deploying our applications using the Gunicorn webserver let's Run:  `pip install gunicorn`

    Procfile is exceedingly simple. It only needs to include one line to instruct Heroku correctly add `web: gunicorn app:app` line to Procfile file.

# Database Manage & Migrations on Heroku

  The following commands to install Migrations packages to manage database schema:
    1. `pip install flask_script`
    2. `pip install flask_migrate`
    3. `pip install psycopg2-binary`

    Run our local migrations using our manage.py file, to mirror how Heroku will run behind the scenes for us when we deploy our application:
      python3 manage.py db init
      python3 manage.py db migrate
      python3 manage.py db upgrade

# Deploying to Heroku
 * Create Heroku app
   in order to create the Heroku app run `heroku create name_of_your_app`. The output will include a git url for your Heroku application.
   
 * Add git remote for Heroku repository
   Using the git url obtained from the last step, in terminal run: `git remote add heroku heroku_git_url`.

 * Add postgresql add on for our database
   Heroku has an addon for apps for a postgresql database instance. Run this code in order to create your database and connect it to your application: heroku addons:`create heroku-postgresql:hobby-dev --app name_of_your_application`

   Run `heroku config --app name_of_your_application` in order to check your configuration variables in Heroku.

 * Push it!
   Push it up! `git push heroku master`

 * Run migrations
   Once your app is deployed, run migrations by running: `heroku run python3 manage.py db upgrade --app name_of_your_application`


 # To test the error handling for aplicationsimply run commands below locally on the machine 
  `source setup.sh && python3 test_app.py`
  or
  `bash setup.sh && python3 test_app.py`




# Testing API in Postman 

After building the full aplication the output would look something similar show below:

**************************   GET  **************************

https://capstone-smith.herokuapp.com/actors
{
    "actors": [
        {
            "age": 19,
            "gender": "female",
            "id": 3,
            "name": "Nency"
        },
        {
            "age": 25,
            "gender": "male",
            "id": 1,
            "name": "sam smith"
        },
        {
            "age": 35,
            "gender": "male",
            "id": 2,
            "name": "smith john"
        },
        {
            "age": 30,
            "gender": "female",
            "id": 4,
            "name": "Zora"
        }
    ],
    "success": true
}

https://capstone-smith.herokuapp.com/movies
{
    "movies": [
        {
            "id": 1,
            "release_date": "Wed, 04 Sep 2019 00:00:00 GMT",
            "title": "Avengers"
        },
        {
            "id": 3,
            "release_date": "Fri, 28 Sep 2012 00:00:00 GMT",
            "title": "Looper"
        },
        {
            "id": 4,
            "release_date": "Wed, 20 Oct 1999 00:00:00 GMT",
            "title": "One piece"
        },
        {
            "id": 2,
            "release_date": "Sat, 08 Mar 2014 00:00:00 GMT",
            "title": "predestination"
        }
    ],
    "success": true
}



**************************   DELETE  **************************

https://capstone-smith.herokuapp.com/actors/1

{
    "actors": [
        {
            "age": 19,
            "gender": "female",
            "id": 3,
            "name": "Nency"
        },
        {
            "age": 35,
            "gender": "male",
            "id": 2,
            "name": "smith john"
        },
        {
            "age": 30,
            "gender": "female",
            "id": 4,
            "name": "Zora"
        }
    ],
    "success": true
}

https://capstone-smith.herokuapp.com/movies/1

{
    "movies": [
        {
            "id": 2,
            "release_date": "Tue, 10 Mar 1998 00:00:00 GMT",
            "title": "JOJO's Adventure"
        },
        {
            "id": 3,
            "release_date": "Fri, 28 Sep 2012 00:00:00 GMT",
            "title": "Looper"
        },
        {
            "id": 4,
            "release_date": "Wed, 20 Oct 1999 00:00:00 GMT",
            "title": "One piece"
        }
    ],
    "success": true
}


**************************   POST  **************************

https://capstone-smith.herokuapp.com/actors

{
    "actor": {
        "age": 41,
        "gender": "male",
        "id": 5,
        "name": "Jerry"
    },
    "success": true
}

https://capstone-smith.herokuapp.com/movies

{
    "movie": {
        "id": 1,
        "release_date": "Fri, 10 Jan 2020 00:00:00 GMT",
        "title": "Re:Zero"
    },
    "success": true
}

**************************   PATCH  **************************

https://capstone-smith.herokuapp.com/actors/5
{
    "age": 35,
    "gender": "male",
    "id": 5,
    "name": "Albetino"
}

https://capstone-smith.herokuapp.com/movies/2
{
    "id": 2,
    "release_date": "Sun, 10 Mar 1998 00:00:00 GMT",
    "title": "JOJO's Adventure"
}
        

############################################################################################################################

######## Side Notes

To check db on local machine teminal run => `heroku pg:psql`   

curl example link: https://reqbin.com/req/c-dwjszac0/curl-post-json-example

# GET movies
curl --location --request GET 'https://capstone-smith.herokuapp.com/movies' \     
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9jOWg1clVFSGVYVmVBanRLcmRPQiJ9.eyJpc3MiOiJodHRwczovL3NjLWZzbmQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmN2I3ODg5YjQ5OGUyMDA2Yjk0NTczYSIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjAyMzQ2OTc0LCJleHAiOjE2MDIzNTQxNzQsImF6cCI6Im5RSW5ReFR0RHJHcFpQUTV4YVloekZvZ1JrSlpTYldmIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6YWN0b3JfZnJvbV9tb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIiwicG9zdDphY3Rvcl90b19tb3ZpZSJdfQ.Oh9OQXWw2EP_IO0uZLvjMDGgG1GdH9ao8Mb5fhK8p_oNQjVQwHKMexeFXfkUtb3GO2W88_utUcPbmwov7ZAGwgW7GU9vEj3UQSMIY96YlLtwcRSJ9k9B474fFKCB3Rj41w9vhnaT6MPeFGJvnfxNryeQojR_r9PMn5FT3d-kY3uTwHzR3IXLEGbpkWE5km2W33PpCWHC1jIezsgvIOAI-u4-kLSvQdCYcXvJdNvDFwfaoGbzJhemgzEUzGs7woMciOecn4oPwvhIGrGjli8owgb7DwtaJ7Y98C1NMnDwQ8NJwfmrL6mVQ64DFztXqPmqC_FxjGh5F6ln7g-HzYldgg'

{"movies":[{"id":1,"release_date":"Wed, 04 Sep 2019 00:00:00 GMT","title":"Avengers"},{"id":3,"release_date":"Fri, 28 Sep 2012 00:00:00 GMT","title":"Looper"},{"id":4,"release_date":"Wed, 20 Oct 1999 00:00:00 GMT","title":"One piece"},{"id":2,"release_date":"Sat, 08 Mar 2014 00:00:00 GMT","title":"predestination"}],"success":true}

############################################################################################################################




