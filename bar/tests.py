"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class BarTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(200, resp.status_code)

    def test_create(self):
        post = {
                'question'  : 'What is your name?',
                'Submit'    : 'submit'
        }
        resp = self.client.post('/new/', post, follow=True)
        self.assertEqual('What is your name?\n', resp.content)

        self.assertEqual(302, resp.redirect_chain[0][1])
        self.assertEqual('http://testserver/1/', resp.redirect_chain[0][0])

        self.assertEqual(('Content-Type', 'text/html; charset=utf-8'), resp._headers['content-type'])
