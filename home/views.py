from django.http import HttpResponse


def index(request):
    return HttpResponse('{"message":"Welcome to The TaskMe API!"}')