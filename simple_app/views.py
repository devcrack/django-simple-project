from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse

@method_decorator(csrf_exempt, name='dispatch')
class FirstPageView(TemplateView):
    template_name = "page-1.html"

    def get_context_data(self, *args, **kwargs):
        self.context = super(FirstPageView, self).get_context_data()
        self.context['PAGE_TITLE'] = "First_Page"
        return self.context

    def get(self, request, *args, **kwargs):
        self.get_context_data(request)
        return self.render_to_response(self.context)

    def post(self, *args, **kwargs):
        if not self.request.POST:
            return redirect("first_page")
        name = self.request.POST['names']
        address = self.request.POST['address']
        phone = self.request.POST['phone']
        return redirect(reverse('second_page', kwargs={'name': name, 'address': address, 'phone': phone}))


class SecondPage(TemplateView):
    template_name = "page-2.html"

    def get_context_data(self, *args, **kwargs):
        self.context = super(SecondPage, self).get_context_data()
        self.context['PAGE_TITLE'] = "Second Page"
        return self.context

    def get(self, request, *args, **kwargs):
        self.get_context_data(request)
        self.context['data'] = [f"{data}:  {kwargs[data]}" for data in kwargs]
        return self.render_to_response(self.context)
