from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import *

def index(request):
    latest_question_list = Question.objects.all()
    return render(request, 'polls/index.html', {
        'latest_question_list': latest_question_list
    })

def detail(request, question_id):
#esto es una manera de hacerlo pero no maneja el 404
    #question = Question.objects.filter(pk=question_id)
#si question trae algo de la db cool, si no 404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {
        'question': question
    })

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {
        'question': question
    })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)   
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'No elegiste una respuesta'
        })
    else:
        #sumamos 1 voto a la variable selected_choice en su modulo(columna de db)
        #votes
        selected_choice.votes += 1
        #con esto guardamos ese voto dentro de la db perse con la funcion save()
        #de django
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.question_id,)))
