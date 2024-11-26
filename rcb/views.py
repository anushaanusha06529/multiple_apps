from django.shortcuts import render
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>king kohili is captain of rcb</h1>')

