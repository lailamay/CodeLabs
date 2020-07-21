from django.db import models

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
