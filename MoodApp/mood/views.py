from django.shortcuts import render
from mood.models import Mood
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .utils.token_generator import Token

def sendMood(request, token):
    try:
        t = Mood.objects.get(pk=token)
    except Mood.DoesNotExist:
        raise Http404("Wrong request. Please make sure to use the right link")
    return render(request, "mood.html", {"mood":t})
