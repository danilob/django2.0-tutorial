from django import forms
from django.forms import ModelForm
from .models import Action

class ActionForm(ModelForm):
    class Meta:
        model = Action
        fields = '__all__'

    notes = forms.CharField(widget=forms.Textarea,required=False)

    def clean_priority(self):
        data = self.cleaned_data['priority']
        if data>5:
            raise forms.ValidationError("A prioridade tem que ser menor que 5!")
        if data<0:
            raise forms.ValidationError("A prioridade tem que ser maior que 0!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data

    def clean_description(self):
        data = self.cleaned_data['description']
        if len(data)>105:
            raise forms.ValidationError("Descrição muito longa!")
        
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data