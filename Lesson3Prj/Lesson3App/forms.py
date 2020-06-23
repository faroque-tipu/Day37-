from django import forms
from Lesson3App.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        