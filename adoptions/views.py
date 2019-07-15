from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return HttpResponse('<p>home view</p>')

def pet_detail(req, id):
    return HttpResponse('<p>pet_detail view with id {}</p>'.format(id))
