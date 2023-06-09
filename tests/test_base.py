import os
import unittest
from flask_testing import TestCase
from flask import url_for, current_app
from main import app

os.system('clear')


class MainTest(TestCase):

    
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        
        return app

    def test_hello(self):
        self.assertEqual('Hello','Hello')
        
    def test_current_app(self):
        self.assertIsNotNone(current_app)
    
    def test_exists_endpoint(self):
        response = self.client.get(url_for('auth.login'))
        self.assertTrue(response.status)
        

        
    
