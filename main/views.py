from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class FormuleView(TemplateView):
    template_name = 'formule.html'


class DarkView(TemplateView):
    template_name = 'dark.html'


class FormView(TemplateView):
    template_name = 'connexion.html'


class SuccessView(TemplateView):
    template_name = 'success.html'
