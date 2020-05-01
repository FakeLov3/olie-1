from django.db import models


class Question(models.Model):

    text = models.TextField()
    label = models.ForeignKey(
        'Label', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.text}'


class Answer(models.Model):

    text = models.TextField() 
    label = models.ForeignKey(
        'Label', blank=True, null=True, on_delete=models.SET_NULL)
    is_suggestion = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'


class Label(models.Model):

    identifier = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.identifier}'