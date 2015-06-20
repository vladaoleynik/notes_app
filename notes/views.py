from django.shortcuts import render
from django.views.generic import TemplateView
import actions
import mixins


# Create your views here.
class IndexView(mixins.NavigationMixin, TemplateView):
    template_name = 'notes/notes.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        notes = actions.get_notes_list()
        notes = actions.pagination(self.request, notes)
        context['notes'] = notes

        return context


class MyNotesView(mixins.NavigationMixin, TemplateView):
    template_name = 'notes/notes.html'

    def get_context_data(self, **kwargs):
        context = super(MyNotesView, self).get_context_data(**kwargs)

        notes = actions.get_author_notes(str(self.request.user))
        notes = actions.pagination(self.request, notes)
        context['notes'] = notes

        return context


class MyCategoriesView(mixins.NavigationMixin, TemplateView):
    template_name = 'notes/settings.html'

    def get_context_data(self, **kwargs):
        context = super(MyCategoriesView, self).get_context_data(**kwargs)

        settings = actions.get_my_settings(str(self.request.user))
        context['settings'] = settings
        print context
        return context


class NotesAuthorView(mixins.NavigationMixin, TemplateView):
    template_name = 'notes/notes.html'

    def get_context_data(self, **kwargs):
        context = super(NotesAuthorView, self).get_context_data(**kwargs)

        author = kwargs['username']
        notes = actions.get_author_notes(kwargs['username'])
        notes = actions.pagination(self.request, notes)
        info = "All author notes: " + author

        context['notes'] = notes
        context['info'] = info

        return context


class NotesCategoryView(mixins.NavigationMixin, TemplateView):
    template_name = 'notes/notes.html'

    def get_context_data(self, **kwargs):
        context = super(NotesCategoryView, self).get_context_data(**kwargs)

        category = kwargs['category']
        notes = actions.get_category_notes(category)
        notes = actions.pagination(self.request, notes)
        info = "All notes by category: " + category

        context['notes'] = notes
        context['info'] = info

        return context


class NotesTagView(mixins.NavigationMixin, TemplateView):
    template_name = 'notes/notes.html'

    def get_context_data(self, **kwargs):
        context = super(NotesTagView, self).get_context_data(**kwargs)

        tag = kwargs['tag']
        notes = actions.get_tag_notes(kwargs['tag'])
        notes = actions.pagination(self.request, notes)
        info = "All notes by tag: " + tag

        context['notes'] = notes
        context['info'] = info

        return context


class NoteView(mixins.NavigationMixin, TemplateView):
    template_name = 'notes/single_note.html'

    def get_context_data(self, **kwargs):
        context = super(NoteView, self).get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        note = actions.get_note(pk)
        context['note'] = note

        return context
