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
    color = forms.ChoiceField()
    """
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES
    )
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES
    )"""

    def send_note(self, user, data):
        print data