import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Actor, Movie, setup_db, db_drop_and_create_all, db
from auth import AuthError, requires_auth

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def home():
        return jsonify({
            'success': True,
            'condition': 'app is running under smith!'
        }), 200

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(payload):

        try:    
            all_actors = Actor.query.order_by(Actor.name).all()
            return_actors = [actors.format() for actors in all_actors]
            return jsonify({
                'success': True,
                'actors': return_actors
            }), 200
        except:
            abort(500)
    
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(payload):

        try:    
            all_movies = Movie.query.order_by(Movie.name).all()
            return_movie = [movies.format() for movies in all_movies]
            return jsonify({
                'success': True,
                'movies': return_movie
            }), 200
        except:
            abort(500)

    
    return app

app = create_app()

'''if __name__ == '__main__':
    app.run()'''

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)