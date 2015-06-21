__author__ = 'vladaoleynik'
from django import forms
import actions


class SettingForm(forms.Form):

    setting = forms.CharField(max_length=30)

    def send_setting(self, user, data, setting):
        return actions.post_my_settings(user, data, setting)


class ColorForm(forms.Form):

    setting = forms.CharField(
        max_length=7,
        help_text='HEX color, as #RRGGBB'
    )

    def send_color(self, user, data):
        return actions.post_my_color(user, data)


class NewNoteForm(forms.Form):

    title = forms.CharField(max_length=40)
    text = forms.CharField(
        widget=forms.Textarea
    )
    color = forms.ChoiceField(
        widget=forms.Select,
        choices=(('---', 'No colors available'),)
    )
    tag = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=(('---', 'No tags available'),)
    )
    category = forms.ChoiceField(
        widget=forms.Select,
        choices=(('---', 'No categories available'),)
    )

    def __init__(self, *args, **kwargs):
        self.declared_fields['color'].choices = kwargs.get('color_choices')
        self.declared_fields['tag'].choices = kwargs.get('tag_choices')
        self.declared_fields['category'].choices = kwargs.get('category_choices')
        return super(NewNoteForm, self).__init__()

    def send_note(self, user, data):
        print data