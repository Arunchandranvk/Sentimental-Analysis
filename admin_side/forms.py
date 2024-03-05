from django import forms
from .models import *

class LogForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","class":"form-control","style":"border-radius: 0.75rem; "}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control","style":"border-radius: 0.75rem; "}))


class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs
        fields = ['post','exp','qual','last_date','description']
        widgets={
            'post':forms.TextInput(attrs={"placeholder":"Post Name","class":"form-control","style":"border-radious:0.75rem;"}),
            'exp':forms.NumberInput(attrs={"placeholder":"Experience","class":"form-control","style":"border-radious:0.75rem;"}),
            'qual':forms.TextInput(attrs={"placeholder":"Qualification","class":"form-control","style":"border-radious:0.75rem;"}),
            'last_date':forms.DateInput(attrs={"placeholder":"Closing Date","class":"form-control","style":"border-radious:0.75rem;"}),
            'description':forms.Textarea(attrs={"placeholder":"Description","class":"form-control","style":"border-radious:0.75rem;"}),
        }        

        