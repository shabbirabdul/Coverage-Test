from django import forms
from models import *

class AddSubscriberForm(forms.Form):
    
    email = forms.EmailField(max_length=254, label="3) Email:", required=True)
    fname = forms.CharField(max_length=25, label="1) First Name:", required=True)
    lname = forms.CharField(max_length=25, label="2) Last Name:", required=True)    
    SECTORS = (('-',  'All'),
               ('AG', 'Agriculture'),
               ('FR', 'Forestry'))
    sector = forms.ChoiceField(choices=SECTORS, label="4) Resource Sector:", initial="-")
    #range = forms.IntegerField(min_value=0)
    coord = forms.CharField(max_length=200, required=True)


    def clean(self):
        cleaned_data = self.cleaned_data

        email = cleaned_data.get("email")
        fname = cleaned_data.get("fname")
        lname = cleaned_data.get("lname")
        sector = cleaned_data.get("sector")
        #range = cleaned_data.get("range")
        coord = cleaned_data.get("coord")

        return cleaned_data