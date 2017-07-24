from django.shortcuts import render
from mood.models import Mood
from django.shortcuts import render
from django.http import HttpResponse

def sendMood(request, token):
    html = "<b> Your token is {}<b>".format(token)
    return HttpResponse(content=html, status=201)
