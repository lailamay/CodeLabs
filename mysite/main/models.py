from django.db import models
from django.contrib.auth.models import AbstractUser


class ScenarioList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#scenario is part of scenariolist, so if list gets deleted,
#individual scenarios get deleted
class Scenario(models.Model):
    scenariolist = models.ForeignKey(ScenarioList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    answer = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.text



class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
