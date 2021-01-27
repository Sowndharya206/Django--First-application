from django import forms  
from myapp.models import workers
  
class wrkForm(forms.ModelForm):  
    class Meta:  
        model = workers  
        fields = "__all__"  
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100) 