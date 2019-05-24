from django.http import HttpResponse
from django.shortcuts import redirect
import hashlib

from shortener.forms import urlForm
from shortener.models import Urls


def index(request):
    link = request.GET.get('link')

    url = Urls(originalUrl=link)
    url.save()
    newLink = '/shortener/' + str(Urls.objects.last().auto_increment_id)
    #return HttpResponse('<a href="' + newLink + '">' + newLink + '</a>', content_type='text/html')
    return HttpResponse( request.META['HTTP_HOST'] + newLink, content_type='text/html')


def get_original(request, page_alias):
    print(page_alias)
    original_link = Urls.objects.filter(auto_increment_id=page_alias)[0].originalUrl
    print(original_link)
    return redirect(original_link)
