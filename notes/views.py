from django.shortcuts import render
from django.views.generic import TemplateView
import actions


# Create your views here.
class IndexView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        notes = actions.get_notes_list()
        return render(request, self.template_name, {'notes': notes})


class NotesAuthorView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        notes = actions.get_author_notes(kwargs['username'])
        return render(request, self.template_name, {'notes': notes})


class NotesCategoryView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        notes = actions.get_category_notes(kwargs['category'])
        return render(request, self.template_name, {'notes': notes})


class NotesTagView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        notes = actions.get_tag_notes(kwargs['tag'])
        return render(request, self.template_name, {'notes': notes})