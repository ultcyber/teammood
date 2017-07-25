from django.shortcuts import render
from mood.models import Mood
from django.shortcuts import render
from django.http import HttpResponse
from .utils.token_generator import Token

def sendMood(request, token):
    random_token = Token().getToken()
    html = "<b> Your token is {}<b>. I generated a random token = {}".format(token, random_token)
    return HttpResponse(content=html, status=201)
