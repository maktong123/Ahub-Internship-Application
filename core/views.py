from django.shortcuts import render, redirect
from datetime import date



def index(request):
    return render(request, "index.html")