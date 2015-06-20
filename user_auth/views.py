from django.shortcuts import render
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView, View
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
class LogOutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class SignInFormView(FormView):
    template_name = 'user_auth/login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        self.success_url = request.GET.get('next', '/')
        return super(SignInFormView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(SignInFormView, self).form_valid(form)

