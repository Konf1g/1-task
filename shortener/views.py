from django.shortcuts import render, redirect
from .forms import urlForm
from .models import Urls
from shortener.forms import *
import hashlib

def index(request):
    # form = urlForm(request.POST)
    # if request.method == "POST" and form.is_valid():
    #     upload = form.cleaned_data
    #     form.save()

    link = request.GET.get('link')
    newDomain = "artyom.ly/"
    hash = hashlib.md5(link.encode()).hexdigest()
    halfHash = hash[0:15]
    newLink = newDomain + halfHash
    values = {
        'newLink': newLink,
    }
    return render(request, 'output.html', values)
