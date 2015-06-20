__author__ = 'vladaoleynik'

import actions


class NavigationMixin(object):

    def get_context_data(self, **kwargs):
        context = super(NavigationMixin, self).get_context_data(**kwargs)
        context['notes_count'] = actions.get_notes_count(self.request.user)
        return context
