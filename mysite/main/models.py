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

    def __str__(self):
        return self.text


class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class User(AbstractUser):
    is_student = models.BooleanField()
    is_teacher = models.BooleanField()

    def __str__(self):
        return self.username


class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
