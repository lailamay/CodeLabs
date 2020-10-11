from django import forms

class CreateNewList(forms.Form): 
    name = forms.CharField(label="Scenario", max_length=300)
    check = forms.BooleanField(required=False)