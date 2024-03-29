"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import os

from django.test import TestCase
from django.test.client import Client
from django.test import LiveServerTestCase
from django.conf import settings

from selenium import webdriver

from bar.models import Avatar


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class BarTest(TestCase):

    fixtures = [
        'test.json'
    ]

    def setUp(self):
        self.client = Client()

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(200, resp.status_code)

    def test_index_queryset(self):
        resp = self.client.get('/')
        expected_qs = ["What is the air speed velocity of an unladen swallow?", ]
        self.assertQuerysetEqual(resp.context['object_list'], expected_qs, lambda x: x.question)

    def test_create(self):
        post = {
                'question'  : 'What is your name?',
                'Submit'    : 'submit'
        }
        resp = self.client.post('/new/', post, follow=True)
        self.assertEqual('What is your name?\n', resp.content)

        self.assertEqual(302, resp.redirect_chain[0][1])
        self.assertTrue(resp.redirect_chain[0][0].startswith('http://testserver/'))

        self.assertEqual(('Content-Type', 'text/html; charset=utf-8'), resp._headers['content-type'])

    def test_create_avatar(self):

        path = os.path.join(settings.PROJECT_ROOT, 'bar/files/test.png')
        image_file = file(path)

        post = {
                'image'     : image_file,
                'name'      : 'test-name'
        }
        resp = self.client.post('/new/avatar', post, follow=True)
        self.assertEqual(200, resp.status_code)

    def test_avatar_unicode(self):
        avatar = Avatar.objects.get(pk=1)
        self.assertTrue(unicode(avatar))

    def test_avatar_update(self):
        avatar = Avatar.objects.get(pk=1)
        self.assertRaises(NotImplementedError, avatar.update)


class AdminLoginTest(LiveServerTestCase):
    fixtures = ['users.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = webdriver.Chrome()
        super(AdminLoginTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(AdminLoginTest, cls).tearDownClass()
        cls.selenium.quit()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('tuxcanfly')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('welcome')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
