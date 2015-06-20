from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import actions


# Create your views here.
class IndexView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        notes = actions.get_notes_list()
        paginator = Paginator(notes, 4)  # Show 4 notes per page

        page = request.GET.get('page')
        try:
            notes = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            notes = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            notes = paginator.page(paginator.num_pages)

        # count = actions.get_notes_count(self.request.user)
        return render(request, self.template_name, {'notes': notes})


class MyNotesView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        notes = actions.get_author_notes(str(request.user))
        return render(request, self.template_name, {'notes': notes})


class NotesAuthorView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        author = kwargs['username']
        notes = actions.get_author_notes(kwargs['username'])
        info = "Author notes: " + author
        return render(request, self.template_name, {'notes': notes, 'info': info})


class NotesCategoryView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        category = kwargs['category']
        notes = actions.get_category_notes(category)
        info = "Notes by category: " + category
        return render(request, self.template_name, {'notes': notes, 'info': info})


class NotesTagView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        tag = kwargs['tag']
        notes = actions.get_tag_notes(kwargs['tag'])
        info = "Notes by tag: " + tag
        return render(request, self.template_name, {'notes': notes, 'info': info})
