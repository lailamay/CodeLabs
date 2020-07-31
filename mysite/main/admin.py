from django.contrib import admin
from .models import ScenarioList, Scenario, User, Student
#from django.contrib.auth.admin import UserAdmin



# Register your models here.
admin.site.register(ScenarioList)
admin.site.register(Scenario)
admin.site.register(User)
admin.site.register(Student)

# @admin.register(LogEntry)
# class LogEntryAdmin(admin.ModelAdmin):
#     # to have a date-based drilldown navigation in the admin page
#     date_hierarchy = 'action_time'

#     # to filter the resultes by users, content types and action flags
#     list_filter = [
#         'user',
#         'content_type',
#         'action_flag'
#     ]

#     # when searching the user will be able to search in both object_repr and change_message
#     search_fields = [
#         'object_repr',
#         'change_message'
#     ]

#     list_display = [
#         'action_time',
#         'user',
#         'content_type',
#         'action_flag',
#     ]