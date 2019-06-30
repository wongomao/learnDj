from django.http import HttpResponse

def index(request):
    return HttpResponse("Hell O'Whirled. You are at the polls index.")
