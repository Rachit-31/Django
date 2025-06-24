from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world")

def about(request):
    return HttpResponse("Hello world 2")

def contact(request):
    return HttpResponse("Hello world 3")