from django.forms import *
from .models import journal

class FormInputJournal(ModelForm):
    class Meta:
        model = journal
        fields = "__all__"
        widgets = {
                    'npp': TextInput(attrs={'class': 'form-control'}),
                    'dateReg': TextInput(attrs={'class': "form-control",'type': 'date','format':'%d.%m.%Y'}),
                    'content': TextInput(attrs={'class': "form-control"}),
                    'executor': TextInput(attrs={'class': "form-control"}),
        }
