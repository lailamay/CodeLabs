from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import ScenarioList, Scenario
from .forms import CreateNewList

#This is where we put what we want to show on our app

def index(response, id):
    #scenario_list = ScenarioList.objects.all()
    scenario_list = ScenarioList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for scenario in scenario_list.scenario_set.all():
                if response.POST.get("c" + str(scenario.id)) == "clicked":
                    scenario.complete = True
                else:
                    scenario.complete = False

                scenario.save()

        elif response.POST.get("newScenario"):
            txt = response.POST.get("newScenario")

            if len(txt) > 2:
                scenario_list.scenario_set.create(text=txt, complete=False)
            else:
                print("invalid")
    #context = {'scenario_list': scenario_list}
    #return render(response, 'main/index.html', context)
    return render(response, "main/scenario.html", {"scenario_list":scenario_list})


def home(response):
	return render(response, "main/home.html", {})



def create(response):
    response.user
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            s = ScenarioList(name=n)
            s.save()

        return HttpResponseRedirect("/%i" %s.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})


# def scenario(response, scenariolist_id):
#     scenario_list = get_object_or_404(ScenarioList, pk= scenariolist_id)
#     return render(response, 'main/scenario.html',  {'scenario_list': scenario_list})


def student(response):
     return render(response, 'main/student.html', {})
