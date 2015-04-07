from django.shortcuts import render
from rango.models import Category
# Create your views here.


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'newmessage': "Message for about page"}
    return render(request, 'rango/about.html', context_dict)
