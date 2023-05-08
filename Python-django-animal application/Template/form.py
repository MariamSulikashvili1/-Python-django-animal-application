from django import forms

class NameForm(forms.Form):
    animal_name = forms.CharField(label= Animal_name', max_length=100)




