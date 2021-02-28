from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class FirstPageView(TemplateView):
    template_name = "page-1.html"

    def get_context_data(self, *args, **kwargs):
        self.context = super(FirstPageView, self).get_context_data()
        self.context['PAGE_TITLE'] = "First_Page"
        return self.context

    def get(self, request, *args, **kwargs):
        self.get_context_data(request)
        return self.render_to_response(self.context)
