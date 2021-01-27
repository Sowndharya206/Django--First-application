from django import forms  
from myapp.models import workers
  
class wrkForm(forms.ModelForm):  
    class Meta:  
        model = workers  
        fields = "__all__"  