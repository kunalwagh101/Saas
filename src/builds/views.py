from django.shortcuts import render,HttpResponse
from .models import Path
from django.http import HttpResponse

def index(request):

    Path.objects.create(name=request.path)
    values = Path.objects.all()
    context = { "visits" : values ,
                "no_number_of_visit" : values.count() ,                
                }

    
    return render(request,"chome.html",context)
