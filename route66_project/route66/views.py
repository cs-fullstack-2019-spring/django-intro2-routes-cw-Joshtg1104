from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#I'm having more fun with this than I should. Resonse for if you choose no route
def index(request):
    return HttpResponse("Hello, you wanna see something funny? \nGo to route /gogetthegood. \nIf you wanna be happy, go to /happyhappyjoyjoy route.")
# gogetthegood route response
def gogetthegood(request):
    return HttpResponse("Here you go! A fly marrying a bumblebee. Ha!")
#response to happyhappyjoyjoy route
def happyhappyjoyjoy(request):
    return HttpResponse("I'll teach ya to be happy! I'll teach ya grandmother to suck eggs!")
# Well that didn't work
# def whydidntyoubelieveme(request):
#     return HttpResponse(input("")+"I heard you!")
