__author__ = 'vladaoleynik'

import requests
from models import Note
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

BASE_URL = 'http://localhost:8000'
AUTH = ('vladaoleynik', '123')

"""
Pagination for notes
"""


def pagination(request, data, per_page=4):
    paginator = Paginator(data, per_page)  # Show 4 notes per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
    return data

"""
REST
"""


# Handles GET for multiple objects
def rest_get_data_list(url, auth=None):
    r = requests.get(url=url, auth=auth)
    data = r.json()
    data.reverse()
    return data


# Handles GET for single object
def rest_get_data(url, auth=None):
    r = requests.get(url=url, auth=auth)
    data = r.json()
    return data


# Handles POST
def rest_post_data(url, clear_data, auth=None):
    r = requests.post(url=url, json=clear_data, auth=auth)
    return r


"""
Notes
"""


# Number of user notes
def get_notes_count(user):
    return Note.objects.filter(user__username=user).count()


# List of all the notes
def get_notes_list():
    url = BASE_URL + '/api/notes/'
    return rest_get_data_list(url)


# Notes by author
def get_author_notes(author):
    url = BASE_URL + '/api/notes/author/' + author
    return rest_get_data_list(url)


# Notes by category
def get_category_notes(category):
    url = BASE_URL + '/api/notes/cat/' + category
    return rest_get_data_list(url)


# Notes by tag
def get_tag_notes(tag):
    url = BASE_URL + '/api/notes/tag/' + tag
    return rest_get_data_list(url)


# Get a single note
def get_note(pk):
    url = BASE_URL + '/api/notes/' + pk
    return rest_get_data(url)

"""
User Settings
"""


# Get a list of custom tags
def get_my_tags(user):
    url = BASE_URL + '/api/user/' + user + '/tag/'
    return rest_get_data_list(url, auth=AUTH)


# Get a list of custom colors
def get_my_colors(user):
    url = BASE_URL + '/api/user/' + user + '/color/'
    return rest_get_data_list(url, auth=AUTH)


# Get a list of custom categories
def get_my_categories(user):
    url = BASE_URL + '/api/user/' + user + '/category/'
    return rest_get_data_list(url, auth=AUTH)


# Gets user id
def __get_user_id(user):
    user_id = User.objects.values('pk').get(username=user)
    return user_id['pk']


# Post new custom color
def post_my_color(user, clear_data):
    url = BASE_URL + '/api/user/' + user + '/color/'
    status = __get_user_id(user)
    data = {
        "color": clear_data,
        "status": status
    }
    return rest_post_data(url, data, auth=AUTH)


# Post new custom tag or category
def post_my_settings(user, clear_data, setting):
    url = BASE_URL + '/api/user/' + user + '/' + setting + '/'
    status = __get_user_id(user)
    data = {
        setting: clear_data,
        "status": status
    }
    return rest_post_data(url, data, auth=AUTH)

"""
System Settings
"""


# Get a list of system tags
def get_system_tags():
    url = BASE_URL + '/api/tag/'
    return rest_get_data_list(url, auth=AUTH)


# Get a list of system colors
def get_system_colors():
    url = BASE_URL + '/api/color/'
    return rest_get_data_list(url, auth=AUTH)


# Get a list of system categories
def get_system_categories():
    url = BASE_URL + '/api/category/'
    return rest_get_data_list(url, auth=AUTH)


def colors_choice(user):
    color_list = []
    custom = get_my_colors(user)
    system = get_system_colors()
    for color in custom:
        colors = [color['color'], color['color']]
        color_list.append(tuple(colors))
    for color in system:
        colors = [color['color'], color['color']]
        color_list.append(tuple(colors))
    return tuple(color_list)