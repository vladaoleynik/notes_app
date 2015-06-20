__author__ = 'vladaoleynik'

import requests

BASE_URL = 'http://localhost:8000'


def rest_api_get_data(url):
    r = requests.get(url=url)
    data = r.json()
    data.reverse()
    return data


def get_notes_list():
    url = BASE_URL + '/api/notes/'
    return rest_api_get_data(url)


def get_author_notes(author):
    url = BASE_URL + '/api/notes/author/' + author
    return rest_api_get_data(url)


def get_category_notes(category):
    url = BASE_URL + '/api/notes/cat/' + category
    return rest_api_get_data(url)


def get_tag_notes(tag):
    url = BASE_URL + '/api/notes/tag/' + tag
    return rest_api_get_data(url)