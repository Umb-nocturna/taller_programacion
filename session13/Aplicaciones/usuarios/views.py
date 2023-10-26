from django.shortcuts import render, redirect
from django.contrib.auth import logout

def exit(request):
    logout(request)
    return redirect('inicio')
