from django.http import HttpResponse




def index(request):
    return HttpResponse("this is the page of views2 thanks")
