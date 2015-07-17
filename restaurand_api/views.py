from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def home(request):
    return redirect('api/v1')
