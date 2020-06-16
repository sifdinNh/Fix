from django.http import HttpResponse




def index(request):
    return HttpResponse("your not allowed to get here watch out!")