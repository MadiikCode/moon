from django.shortcuts import render
from .models import Task


def index(request):
    task = Task.objects.order_by('-id')
    return render(request,'main_app/index.html',{'title': 'Главная страница сайта ', 'tasks': task})

def about(request):
    return render(request, 'main_app/about.html')


def profile(request):
    return  render(request,'main_app/')
#def index(request):
 #   data = {
#        'title': 'Главная страница',
 #   }
 #   return render(request, 'main_app/index.html', data)



##def about(request):
  #
    #return render(request, 'main_app/about.html')