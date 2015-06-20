__author__ = 'vladaoleynik'

import requests
from models import Note
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

BASE_URL = 'http://localhost:8000'


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


def get_notes_count(user):
    return Note.objects.filter(user__username=user).count()


def rest_get_data_list(url):
    r = requests.get(url=url)
    data = r.json()
    data.reverse()
    return data


def rest_get_data(url):
    r = requests.get(url=url)
    data = r.json()
    return data


def get_notes_list():
    url = BASE_URL + '/api/notes/'
    return rest_get_data_list(url)


def get_author_notes(author):
    url = BASE_URL + '/api/notes/author/' + author
    return rest_get_data_list(url)


def get_category_notes(category):
    url = BASE_URL + '/api/notes/cat/' + category
    return rest_get_data_list(url)


def get_tag_notes(tag):
    url = BASE_URL + '/api/notes/tag/' + tag
    return rest_get_data_list(url)


def get_note(pk):
    url = BASE_URL + '/api/notes/' + pk
    return rest_get_data(url)