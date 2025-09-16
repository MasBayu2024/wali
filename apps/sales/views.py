from django.http import HttpResponse

def index(request):
    return HttpResponse("Halaman Sales")
