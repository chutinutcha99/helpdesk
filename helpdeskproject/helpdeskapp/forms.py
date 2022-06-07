from django import forms
from .models import AddTicket
from django.forms import widgets

class AddTicketForm(forms.ModelForm):

    class Meta:

        model = AddTicket

        fields = '__all__'

        widgets = {
            'issue_date': widgets.DateInput(attrs={'type': 'date'}),
            'job_complete_date': widgets.DateInput(attrs={'type': 'date'}),
            'give_back_date': widgets.DateInput(attrs={'type': 'date'}),
            'spare_device_date': widgets.DateInput(attrs={'type': 'date'}),
            'got_back_spare_device_date': widgets.DateInput(attrs={'type': 'date'}),
        }

