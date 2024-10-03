from django import forms
from .models import Expense
from django.forms.widgets import DateInput

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'category', 'description', 'amount']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }