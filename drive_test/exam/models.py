from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=200)
    symbol = models.CharField(max_length=1, default='')
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
