from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
import actions
import mixins
from forms import SettingForm, ColorForm, NewNoteForm


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
        context['settings'] = settings['category']
        context['info'] = "No custom categories yet."
        return context

    def post(self, *args, **kwargs):
        print kwargs


class MyTagsView(mixins.NavigationMixin, FormView):
    template_name = 'notes/my_tags.html'
    form_class = SettingForm
    url = reverse_lazy('my_tags')
    success_url = url

    def get_context_data(self, **kwargs):
        context = super(MyTagsView, self).get_context_data(**kwargs)
        system = actions.get_system_tags()
        custom = actions.get_my_tags(str(self.request.user))
        context['system'] = system
        context['custom'] = custom
        context['set'] = "tag"
        return context

    def form_valid(self, form):
        setting = form.cleaned_data['setting']
        self.object = form.send_setting(str(self.request.user), setting, "tag")
        return super(MyTagsView, self).form_valid(form)


class MyCategoriesView(mixins.NavigationMixin, FormView):
    template_name = 'notes/my_categories.html'
    form_class = SettingForm
    url = reverse_lazy('my_categories')
    success_url = url

    def get_context_data(self, **kwargs):
        context = super(MyCategoriesView, self).get_context_data(**kwargs)
        system = actions.get_system_categories()
        custom = actions.get_my_categories(str(self.request.user))
        context['system'] = system
        context['custom'] = custom
        context['set'] = "category"
        return context

    def form_valid(self, form):
        setting = form.cleaned_data['setting']
        self.object = form.send_setting(str(self.request.user), setting, "category")
        return super(MyCategoriesView, self).form_valid(form)


class MyColorsView(mixins.NavigationMixin, FormView):
    template_name = 'notes/my_colors.html'
    form_class = ColorForm
    url = reverse_lazy('my_colors')
    success_url = url

    def get_context_data(self, **kwargs):
        context = super(MyColorsView, self).get_context_data(**kwargs)
        system = actions.get_system_colors()
        custom = actions.get_my_colors(str(self.request.user))
        context['system'] = system
        context['custom'] = custom
        return context

    def form_valid(self, form):
        setting = form.cleaned_data['setting']
        setting = setting.replace('#', '')
        self.object = form.send_color(str(self.request.user), setting)
        return super(MyColorsView, self).form_valid(form)


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


class CreateNoteView(mixins.NavigationMixin, FormView):
    template_name = 'notes/new_note.html'
    form_class = NewNoteForm
    url = reverse_lazy('new_note')
    success_url = url

    def get_context_data(self, **kwargs):
        user = str(self.request.user)
        context = super(CreateNoteView, self).get_context_data(**kwargs)
        system = actions.get_system_colors()
        custom = actions.get_my_colors(user)
        context['system'] = system
        context['custom'] = custom
        context['color_choice'] = actions.colors_choice(user)
        return context

    def form_valid(self, form):
        print 'fdg'
        self.object = form.send_note(str(self.request.user), form.cleaned_data)
        return super(CreateNoteView, self).form_valid(form)
