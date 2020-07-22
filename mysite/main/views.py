from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import ScenarioList, Scenario

#This is where we put what we want to show on our app

def index(response):
    scenario_list = ScenarioList.objects.all()
    #scenario_list = ScenarioList.objects.get(id=id)
    context = {'scenario_list': scenario_list}
    return render(response, 'main/index.html', context)
    #return HttpResponse("<h1>%s</h1>" %scenario_list.name)


def student(response, scenariolist_id):
    try:
        scenario_list = ScenarioList.objects.get(pk=scenariolist_id)
    except ScenarioList.DoesNotExist:
        raise Http404("Scenario does not exist")
    return render(response, 'main/student.html', {'scenario_list': scenario_list})


def scenario(response, scenariolist_id):
    scenario_list = get_object_or_404(ScenarioList, pk= scenariolist_id)
    return render(response, 'main/scenario.html',  {'scenario_list': scenario_list})
