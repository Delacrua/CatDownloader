from django.http import HttpResponse

from . import tasks


__all__ = ['home',
           ]


def home(request):
    tasks.download_a_cat.delay()
    return HttpResponse('<h1> DOWNLOADING A CAT PICTURE </h1>')
