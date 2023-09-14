from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"pages/inicio1.html",{})


def nosotros(request):
    return render(request,"pages/nosotros.html",{})