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

class VaccineListView(ListView):
    template_name = 'vaccines.html'
    queyset = Vaccine.objects.all()
    def get_queryset(self):
         return self.queyset

# Create your views here.
def home(req):
    pets = Pet.objects.all()
    return render(req, 'home.html', {'pets': pets})

def pet_detail(req, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(req, 'pet_detail.html', {'pet': pet})
