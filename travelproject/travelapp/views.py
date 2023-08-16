from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team


def index(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()

    return render(request,'index.html',{'result': obj,'teams':obj1})
