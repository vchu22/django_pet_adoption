from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Pet, Vaccine

# Create your views here.
class home(ListView):
    template_name = 'home.html'
    queyset = Pet.objects.all()
    def get_queryset(self):
        return self.queyset

class VaccineListView(ListView):
    template_name = 'vaccines.html'
    queyset = Vaccine.objects.all()
    def get_queryset(self):
        return self.queyset

class PetDetailView(DetailView):
    model = Pet
    template_name = 'pet_detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'