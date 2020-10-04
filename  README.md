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
   Once your app is deployed, run migrations by running: heroku run `python3 manage.py db upgrade --app name_of_your_application`
   