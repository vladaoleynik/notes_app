from django.shortcuts import render
from django.views.generic import TemplateView, View

import actions


# Create your views here.
class IndexView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        notes = actions.get_notes_list()
        notes = actions.pagination(request, notes)
        # count = actions.get_notes_count(self.request.user)
        return render(request, self.template_name, {'notes': notes})


class MyNotesView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        notes = actions.get_author_notes(str(request.user))
        notes = actions.pagination(request, notes)
        return render(request, self.template_name, {'notes': notes})


class NotesAuthorView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        author = kwargs['username']
        notes = actions.get_author_notes(kwargs['username'])
        notes = actions.pagination(request, notes)
        info = "Author notes: " + author
        return render(request, self.template_name, {'notes': notes, 'info': info})


class NotesCategoryView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        category = kwargs['category']
        notes = actions.get_category_notes(category)
        notes = actions.pagination(request, notes)
        info = "Notes by category: " + category
        return render(request, self.template_name, {'notes': notes, 'info': info})


class NotesTagView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        tag = kwargs['tag']
        notes = actions.get_tag_notes(kwargs['tag'])
        notes = actions.pagination(request, notes)
        info = "Notes by tag: " + tag
        return render(request, self.template_name, {'notes': notes, 'info': info})


class NoteView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        notes = actions.get_note(pk)
        return render(request, self.template_name, {'notes': notes})
