from django import forms
from .models import Contact,Carrers

class ContactForm(forms.Form):
    firstname=forms.CharField(max_length=20)
    email=forms.EmailField(max_length=50)
    message=forms.CharField(max_length=1000)
class contact(forms.Form):
    class Meta:
        model=Contact
        field=('firsname','email','message')
class CarresForm(forms.Form):
    job_title = forms.CharField(max_length=30)
    experience_reqiured = forms.CharField(max_length=8)
    req_skills = forms.CharField(max_length=100)
    job_description = forms.CharField(max_length=1000)
    contact_no = forms.CharField(max_length=10)
class Carresform(forms.Form):
    class Meta:
        model=Carrers
        fields=['id','job_title',' experience_required','req_skills','job_description','contact_no','job_location']
