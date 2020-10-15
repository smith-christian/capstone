import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor
#from dotenv import load_dotenv

#load_dotenv()

class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        #self.database_path = os.environ.get['DATABASE_URL']
        setup_db(self.app, self.database_path)

        ASSISTANT_TOKEN = os.environ.get('ASSISTANT_TOKEN') 
        DIRECTOR_TOKEN = os.environ.get('DIRECTOR_TOKEN')
        PRODUCER_TOKEN = os.environ.get('PRODUCER_TOKEN')


        self.assistant_header = {
            "Authorization": "Bearer {}".format(ASSISTANT_TOKEN)}
        
        self.director_header = {
            "Authorization": "Bearer {}".format(DIRECTOR_TOKEN)}

        self.producer_header = {
            "Authorization": "Bearer {}".format(PRODUCER_TOKEN)}
            

        #print('assistant', self.assistant_header)
        #print('director', self.director_header)
        #print('producer', self.producer_header)



        self.actor = {
            "name": "Will Smith",
            "age": 52,
            'gender': 'male',
            'id': 6
        }

        self.add_actor = {
            "name": "Kit Harington",
            "age": 33,
            'gender': 'male',
            'id': 7
        }

        self.update_actor = {
            "name": "Jon Snow",
            "age": 33,
            'gender': 'male',
            'id': 7
        }

        self.movie = {
            'title': "Honest Thief",
            'release_date': "October 9, 2020",
            'id': 6
        }

        self.add_movie = {
            'title': "The Revenant",
            'release_date': "January 8, 2016",
            'id': 7,
        }

        self.update_movie = {
            'title': "Honest Thief",
            'release_date': "January 8, 2016",
            'id': 7
        }



        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()


    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_home(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["condition"])
    
    def test_401_casting_assistant_actor(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
    
    def test_401_casting_assistant_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    # Tests for casting assistant (GET)
    def test_casting_assistant_get_actor(self):
        res = self.client().get('/actors', headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    '''def test_401_casting_assistant_actor(self):
        res = self.client().get('/actors', headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'unathorized')'''

    def test_casting_assistant_get_movies(self):
        res = self.client().get('/movies', headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    '''def test_401_casting_assistant_movies(self):
        res = self.client().get('/movies', headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'unathorized')'''

    
    # Tests for castins_director (POST/DELETE/PATCH)


    def test_casting_director_get_actor(self):
        res = self.client().get('/actors', headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    '''def test_401_casting_director_movies(self):
        res = self.client().get('/actors', headers=self.adirector_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'unathorized')'''

    def test_post_casting_director_success(self):
        res = self.client().post('/actors', json=self.add_actor, headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_director_patch_actors(self):
        res = self.client().patch('actors/7', json=self.update_actor,
                                  headers=self.director_header)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_director_400_patch_actors(self):
        res = self.client().patch('actors/1', headers=self.director_header)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)
    
    def test_post_casting_director(self):
        res = self.client().post('/actors', json=self.add_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)


    def test_director_delete_actors(self):
        res = self.client().delete('actors/1', headers=self.director_header)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_casting_assistant_get_actor(self):
        res = self.client().get('/movies', headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    '''def test_401_casting_director_movies(self):
        res = self.client().get('/movies', headers=self.adirector_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'unathorized')'''

    def test_director_400_patch_movies(self):
        res = self.client().patch('movies/1', headers=self.director_header)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)

    def test_director_patch_movie(self):
        res = self.client().patch('movies/7', json=self.update_movie,
                                  headers=self.director_header)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    # Tests for PRODUCER (POST/DELETE/PATCH)

    def test_producer_get_actor(self):
        res = self.client().get('/actors', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    '''def test_401_producer_movies(self):
        res = self.client().get('/actors', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'unathorized')'''

    def test_post_producer_success(self):
        res = self.client().post('/actors', json=self.add_actor, headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_producer_patch_actors(self):
        res = self.client().patch('actors/7', json=self.update_actor,
                                  headers=self.producer_header)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_producer_400_patch_actors(self):
        res = self.client().patch('actors/1', headers=self.producer_header)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)
    
    def test_post_producer(self):
        res = self.client().post('/actors', json=self.add_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)


    def test_producer_delete_actors(self):
        res = self.client().delete('actors/1', headers=self.producer_header)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_producer_get_actor(self):
        res = self.client().get('/movies', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    '''def test_401_casting_director_movies(self):
        res = self.client().get('/movies', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data['message'], 'unathorized')'''

    def test_producer_400_patch_movies(self):
        res = self.client().patch('movies/1', headers=self.producer_header)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)

    def test_producer_patch_movie(self):
        res = self.client().patch('movies/7', json=self.update_movie,
                                  headers=self.producer_header)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_404_producer_delete_actors(self):
        res = self.client().delete('movies/1', headers=self.producer_header)

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()