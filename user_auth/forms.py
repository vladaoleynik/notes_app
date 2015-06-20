__author__ = 'vladaoleynik'
from django import forms
import json
import actions
from django.contrib.auth.hashers import make_password


class SignUpForm(forms.Form):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    user = forms.CharField(max_length=40)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput,
                                help_text="Enter the same password as above, for verification.")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def send_email(self):
        data = dict()
        data['username'] = self.cleaned_data['user']
        data['password'] = make_password(self.cleaned_data['password1'])
        print actions.create_user(data)