from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = 
    return HttpResponse('estas en la pagina principal')

def detail(request, question_id):
    return HttpResponse(f'estas viendo la pregunta no. {question_id}')

def results(request, question_id):
    return HttpResponse(f'estas viendo los resultados de la pregunta no. {question_id}')

def vote(request, question_id):
    return HttpResponse(f'estas votando a la pregunta no. {question_id}')
