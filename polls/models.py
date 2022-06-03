from django.db import models

#class Question(models.Model):
#    """el atributo id nos lo podemos saltar ya que el orm de python lo tiene
#    autoconfigurado para autoimplementarce y que tenga el contador autoincremental"""
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')

#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)

#-----------------------aprendiendo ORM--------------------------

#--------------trayendo los modelos de mysql legacy--------------

class Choice(models.Model):
    choice_id = models.AutoField(primary_key=True)
    question = models.ForeignKey('Question', models.DO_NOTHING)
    choice_text = models.CharField(max_length=400, blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.choice_text

    class Meta:
        managed = False
        db_table = 'choice'


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=400, blank=True, null=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text

    class Meta:
        managed = False
        db_table = 'question'


# Create your models here.
