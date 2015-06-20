from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import FormView, View
from user_auth.forms import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response
from django.template.context_processors import csrf


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


class SignUpFormView(FormView):
    template_name = 'user_auth/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        return super(SignUpFormView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.send_email()
        username = form.cleaned_data['user']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect('/')
        return HttpResponseRedirect('/auth/signup')

