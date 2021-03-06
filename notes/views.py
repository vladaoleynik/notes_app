from django.shortcuts import render
from django.views.generic import TemplateView, FormView, View
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import os
from datetime import datetime
import actions
import mixins
from forms import SettingForm, ColorForm, NewNoteForm


# Create your views here.
class IndexView(mixins.NavigationMixin, TemplateView):
    template_name = 'notes/notes.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        notes = actions.get_notes_exclude_user(str(self.request.user))
        notes = actions.pagination(self.request, notes)
        context['notes'] = notes
        context['MEDIA_URL'] = settings.MEDIA_URL

        return context


class MyNotesView(mixins.NavigationMixin, TemplateView):
    template_name = 'notes/my_notes.html'

    @method_decorator(login_required(login_url=reverse_lazy('signin')))
    def dispatch(self, request, *args, **kwargs):
        return super(MyNotesView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MyNotesView, self).get_context_data(**kwargs)

        notes = actions.get_author_notes(str(self.request.user))
        notes = actions.pagination(self.request, notes)
        context['notes'] = notes
        context['MEDIA_URL'] = settings.MEDIA_URL

        return context


class MyTagsView(mixins.NavigationMixin, FormView):
    template_name = 'notes/my_tags.html'
    form_class = SettingForm
    url = reverse_lazy('my_tags')
    success_url = url

    @method_decorator(login_required(login_url=reverse_lazy('signin')))
    def dispatch(self, request, *args, **kwargs):
        return super(MyTagsView, self).dispatch(request, *args, **kwargs)

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

    @method_decorator(login_required(login_url=reverse_lazy('signin')))
    def dispatch(self, request, *args, **kwargs):
        return super(MyCategoriesView, self).dispatch(request, *args, **kwargs)

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

    @method_decorator(login_required(login_url=reverse_lazy('signin')))
    def dispatch(self, request, *args, **kwargs):
        return super(MyColorsView, self).dispatch(request, *args, **kwargs)

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
        context['MEDIA_URL'] = settings.MEDIA_URL

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
        context['MEDIA_URL'] = settings.MEDIA_URL

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
        context['MEDIA_URL'] = settings.MEDIA_URL

        return context


class CreateNoteView(mixins.NavigationMixin, FormView):
    template_name = 'notes/new_note.html'
    form_class = NewNoteForm
    url = reverse_lazy('my_notes')
    success_url = url

    def get_context_data(self, **kwargs):
        user = str(self.request.user)
        context = super(CreateNoteView, self).get_context_data(**kwargs)
        system = actions.get_system_colors()
        custom = actions.get_my_colors(user)
        context['system'] = system
        context['custom'] = custom
        return context

    def get_form_kwargs(self):
        user = str(self.request.user)
        kwargs = super(CreateNoteView, self).get_form_kwargs()
        kwargs['color_choices'] = actions.colors_choice(user)
        kwargs['tag_choices'] = actions.tags_choice(user)
        kwargs['category_choices'] = actions.categories_choice(user)
        return kwargs

    def form_valid(self, form):
        try:
            media = self.request.FILES['media']
        except:
            media = None
        if media:
            media = self.request.FILES['media']
            path = 'uploaded/{0}_{1}'.format(
                datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), media.name
            )
            form.cleaned_data['media'] = path
            path = os.path.join(settings.MEDIA_ROOT, path)
            self._upload_file(path, media)

        self.object = actions.post_my_note(str(self.request.user), form.cleaned_data)
        return super(CreateNoteView, self).form_valid(form)

    def _upload_file(self, path, media):
        with open(path, 'wb') as destination:
            for chunk in media.chunks():
                destination.write(chunk)


class ChangeNoteView(mixins.NavigationMixin, FormView):
    template_name = 'notes/change_note.html'
    form_class = NewNoteForm

    def get_context_data(self, **kwargs):
        user = str(self.request.user)
        context = super(ChangeNoteView, self).get_context_data(**kwargs)

        system = actions.get_system_colors()
        custom = actions.get_my_colors(user)
        context['system'] = system
        context['custom'] = custom

        pk = self.kwargs.get('pk')
        note = actions.get_note(pk)
        context['note'] = note
        context['MEDIA_URL'] = settings.MEDIA_URL

        return context

    def get_form_kwargs(self):
        user = str(self.request.user)

        kwargs = super(ChangeNoteView, self).get_form_kwargs()
        kwargs['color_choices'] = actions.colors_choice(user)
        kwargs['tag_choices'] = actions.tags_choice(user)
        kwargs['category_choices'] = actions.categories_choice(user)

        return kwargs

    def form_valid(self, form):
        try:
            media = self.request.FILES['media']
        except:
            media = None
        if media:
            path = 'uploaded/{0}_{1}'.format(
                datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), media.name
            )
            form.cleaned_data['media'] = path
            path = os.path.join(settings.MEDIA_ROOT, path)
            self._upload_file(path, media)

        note_id = self.kwargs.get('pk')
        self.object = actions.put_my_note(str(self.request.user), note_id, form.cleaned_data)
        return HttpResponseRedirect(self.request.path)

    def _upload_file(self, path, media):
        with open(path, 'wb') as destination:
            for chunk in media.chunks():
                destination.write(chunk)


class DeleteNoteView(View):

    def get(self, request, *args, **kwargs):
        note_id = self.kwargs.get('pk')
        actions.delete_my_note(str(self.request.user), note_id)

        url = reverse_lazy('my_notes')
        return HttpResponseRedirect(url)
