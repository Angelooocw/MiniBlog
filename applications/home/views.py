import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, CreateView

# apps entrada
from applications.entrada.models import Entry
# models
from .models import Home
# forms
from .forms import SubscribersForm, ContactForm


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # cargamos el home
        context['home'] = Home.objects.latest('created')
        # contexto de portada
        context['portada'] = Entry.objects.entrada_en_portada()
        # contexto paraa articulos en home
        context['entradas_home'] = Entry.objects.entradas_en_home()
        # entradas recientes
        context['entradas_recientes'] = Entry.objects.entradas_recientes()
        # enviar formulario de suscripcion
        context['form'] = SubscribersForm
        return context


class SubsCreateView(CreateView):
    form_class = SubscribersForm
    success_url = '.'


class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'
    
