from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    context_dict={'boldmessage':"Bold message from dictionary"}
    return render(request,'rango/index.html', context_dict)

def about(request):
    context_dict={'newmessage':"Message for about page"}
    return render(request,'rango/about.html', context_dict)
