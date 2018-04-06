from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the activities index.")

def detail(request, question_id):
    return HttpResponse("You're looking the shedule %s." % question_id)

def listactions(request, question_id):
    response = "You're looking at the list actions of the schedule %s."
    return HttpResponse(response % question_id)

def priority(request, question_id):
    return HttpResponse("You're changing the priority of the schedule's action  %s." % question_id)