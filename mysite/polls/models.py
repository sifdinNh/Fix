from django.db import models
from django.utils import timezone

# Create your models here.
class ads(models.Model):
    centent=models.CharField(max_length=200)
    image=models.FileField(upload_to='images/',blank=True,null=True)
    created_date=models.DateTimeField('ads created date',default=timezone.now())
    def time_created(self):
        a=timezone.now()-self.created_date

        return a

    def __str__(self):
        return self.centent


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


