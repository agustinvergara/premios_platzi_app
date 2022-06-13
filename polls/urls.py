from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    #ex: ''/ we are in the index
    path('', views.index, name='index'),
    #ex: polls/5/ we are seeing the details of the question #5 (question_id)
    path('<int:question_id>/', views.detail, name='detail'),
    #ex: /polls/5/results/ we are seeing the results of the question #5 (question_id)
    path('<int:question_id>/results/', views.results, name='results'),
    #ex: polls/5/vote/ we are voting for the question #5 (question_id)
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
