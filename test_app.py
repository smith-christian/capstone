import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

ASSISTANT_TOKEN = os.environ.get('ASSISTANT_TOKEN') 

class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)


        self.assistant_header = {
            "Authorization": "Bearer {}".format(ASSISTANT_TOKEN)}
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def home(self):
        res = self.client().get('/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["condition"])

    # Tests for casting assistant
    def get_casting_assistant(self):
        res = self.client().get('/actors', headers=self.assistant_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data['actors'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()