import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor


class CastingAgencyTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.producer_headers = {
            "Content-Type": "application/json",
            "Authorization":  os.environ.get('EXECUTIVE_PRODUCER')
        }
        self.assistant_headers = {
            "Content-Type": "application/json",
            "Authorization":  os.environ.get('CASTING_ASSISTANT')
        }

        self.new_actor = {
            'name': 'karim',
            'age': 23,
            'gender': 'male'
        }
        self.new_movie = {
            'title': 'Avengers4'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    ###########
    # Test Actor get
    ###################
    def test_get_all_actors(self):
        res = self.client().get(
            '/actors', headers={"Authorization": "Bearer {}".
                                format(self.producer_headers)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertTrue(data['message'], 'unathorized' )



# Make the tests conveniently executable
if __name__ == "__main__":
  unittest.main()