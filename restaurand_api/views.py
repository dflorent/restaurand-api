from django.http import HttpResponse
from django.shortcuts import redirect


def home(request):
    return HttpResponse('go to /api/v1') 
