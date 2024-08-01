from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world, this is the beginning of a trader app")