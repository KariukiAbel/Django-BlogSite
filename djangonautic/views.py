from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Home page")

def about(request):
    return HttpResponse("about")
