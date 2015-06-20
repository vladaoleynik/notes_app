__author__ = 'vladaoleynik'
import requests
import json

BASE_DIR = 'http://localhost:8000'
AUTH = ('vladaoleynik', '123')


def create_user(clear_data):
    url = BASE_DIR + '/api/user/'
    r = requests.post(url=url, json=clear_data)
    return r
