from django.shortcuts import render

# Create your views here.


#def inicio(request):
#    return render(request,"inicio.html",{})

def inicio(request):
    return render(request,"pages/inicio.html",{})

def resumen(request):
    return render(request,"pages/resumen.html",{})