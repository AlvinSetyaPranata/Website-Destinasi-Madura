from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req, *args, **kwargs):
    # return HttpResponse("<h1> Hello Worlds </h1>")
    return render(req, "home/index.html")