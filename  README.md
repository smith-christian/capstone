# Getting Started on Heroku

Before we can do anything with Heroku, we need to do two things. First, we need to create an account with Heroku here and then we need to download the Heroku CLI (Command Line Interface) in order to run commands from the terminal that enable us to create a Heroku application and manage it.

After you create your account, install Heroku with Homebrew by running:

`brew tap heroku/brew && brew install heroku`

If you need alternate instructions for the download they can be found here. You can verify the download by typing which heroku.

# Deployment Configuration:
 * Installing Dependencies
    Deploying an application to Heroku is as simple as pushing that repository to Heroku, just like Github. Heroku does a lot of things behind the scenes for us when we push a repository - including installing dependencies. For a Python application, Heroku looks for a requirements.txt file that needs to include all of your dependencies.

    `pip freeze > requirements.txt`

 * Environment Configuration
    If you're following along in the project, use `touch setup.sh` and set up all of your environment variables in that file.

 * Gunicorn
    Gunicorn is a pure-Python HTTP server for WSGI applications. We'll be deploying our applications using the Gunicorn webserver.

    First, we need to install gunicorn using `pip install gunicorn`. Next `touch Procfile` to create the file.

    Procfile is exceedingly simple. It only needs to include one line to instruct Heroku correctly for us: `web: gunicorn app:app`. Just make sure your app is housed in app.py as it is in the sample project. Go ahead and make those updates to the sample project if you're following along.

# Database Manage & Migrations on Heroku
    In the data modeling course, you learned how to use migrations to manage your database schema and changes that you make to it. Heroku can run all your migrations to the database you have hosted on the platform, but in order to do so, your application needs to include a manage.py file.

    We'll need three new packages in the file. Run the following commands to install them:

   1. `pip install flask_script`
   2. `pip install flask_migrate`
   3. `pip install psycopg2-binary`

    Now we can run our local migrations using our manage.py file, to mirror how Heroku will run behind the scenes for us when we deploy our application:

    python3 manage.py db init
    python3 manage.py db migrate
    python3 manage.py db upgrade

    Those last commands are the essential process that Heroku will run to ensure your database is architected properly. We, however, won't need to run them again unless we're testing the app locally.
    
# Deploying to Heroku
 * Create Heroku app
   in order to create the Heroku app run `heroku create name_of_your_app`. The output will include a git url for your Heroku application. Copy this as, we'll use it in a moment.
   
 * Add git remote for Heroku to local repository
   Using the git url obtained from the last step, in terminal run: `git remote add heroku heroku_git_url`.

 * Add postgresql add on for our database
   Heroku has an addon for apps for a postgresql database instance. Run this code in order to create your database and connect it to your application: heroku addons:`create heroku-postgresql:hobby-dev --app name_of_your_application`

   Run `heroku config --app name_of_your_application` in order to check your configuration variables in Heroku.

 * Push it!
   Push it up! `git push heroku master`

 * Run migrations
   Once your app is deployed, run migrations by running: `heroku run python3 manage.py db upgrade --app name_of_your_application`

# to run app locally 
  `export FLASK_APP=app.py` 
  `flask run --reload`

********************* Heroku CLI *************************

To check db on local machine teminal run => `heroku pg:psql`   


##################### side activity ############################

curl example link: https://reqbin.com/req/c-dwjszac0/curl-post-json-example

# GET movies
curl --location --request GET 'https://capstone-smith.herokuapp.com/movies' \     
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9jOWg1clVFSGVYVmVBanRLcmRPQiJ9.eyJpc3MiOiJodHRwczovL3NjLWZzbmQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmN2I3ODg5YjQ5OGUyMDA2Yjk0NTczYSIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjAyMzQ2OTc0LCJleHAiOjE2MDIzNTQxNzQsImF6cCI6Im5RSW5ReFR0RHJHcFpQUTV4YVloekZvZ1JrSlpTYldmIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6YWN0b3JfZnJvbV9tb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIiwicG9zdDphY3Rvcl90b19tb3ZpZSJdfQ.Oh9OQXWw2EP_IO0uZLvjMDGgG1GdH9ao8Mb5fhK8p_oNQjVQwHKMexeFXfkUtb3GO2W88_utUcPbmwov7ZAGwgW7GU9vEj3UQSMIY96YlLtwcRSJ9k9B474fFKCB3Rj41w9vhnaT6MPeFGJvnfxNryeQojR_r9PMn5FT3d-kY3uTwHzR3IXLEGbpkWE5km2W33PpCWHC1jIezsgvIOAI-u4-kLSvQdCYcXvJdNvDFwfaoGbzJhemgzEUzGs7woMciOecn4oPwvhIGrGjli8owgb7DwtaJ7Y98C1NMnDwQ8NJwfmrL6mVQ64DFztXqPmqC_FxjGh5F6ln7g-HzYldgg'

{"movies":[{"id":1,"release_date":"Wed, 04 Sep 2019 00:00:00 GMT","title":"Avengers"},{"id":3,"release_date":"Fri, 28 Sep 2012 00:00:00 GMT","title":"Looper"},{"id":4,"release_date":"Wed, 20 Oct 1999 00:00:00 GMT","title":"One piece"},{"id":2,"release_date":"Sat, 08 Mar 2014 00:00:00 GMT","title":"predestination"}],"success":true}
