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
            all_movies = Movie.query.order_by(Movie.title).all()
            return_movie = [movies.format() for movies in all_movies]
            return jsonify({
                'success': True,
                'movies': return_movie
            }), 200
        except:
            abort(500)
    
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actor(payload):
        
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        
        try:
            actor = Actor(name = name, age = age, gender = gender)
            actor.insert()

            return jsonify({
                'success': True,
                'actor': actor.format()
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth("delete:actor")
    def delete_actor(payload, actor_id):

        actor = Actor.query.get(actor_id)
        if actor is None:
            abort(404)
        try:
            actor.delete()
            
            return jsonify({
                'success': True,
                'actor_id_delete': drink.id
            })
            abort(200)
        except:
            abort(500)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def patch_actor(payload, actor_id):
        
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404)        
        if name:
            actor.name = name
        if name:
            actor.age = age
        if name:
            actor.gender = gender
        try:
            actor.update()

            return jsonify({
                'success': True,
                'actor': actor.format()
            })
            abort(200)
        except:
            abort(500)

'''    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def patch_actor(payload, movie_id):
        
        body = request.get_json()
        title = body.get('title', None)
        release_date = body.get('release_date', None)

        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404)        
        if title:
            movie.title = title
        if release_date:
            movie.release_date = release_date
        try:
            movie.update()

            return jsonify({
                'success': True,
                'movie': movie.format()
            })
            abort(200)
        except:
            abort(500)'''

    
    return app

app = create_app()

'''if __name__ == '__main__':
    app.run()'''

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)