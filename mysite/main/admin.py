from django.contrib import admin
from .models import ScenarioList, Scenario, User, Student
#from django.contrib.auth.admin import UserAdmin



# Register your models here.
admin.site.register(ScenarioList)
admin.site.register(Scenario)
admin.site.register(User)
admin.site.register(Student)

