from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        notes = dict()
        return render(request, self.template_name, notes)