from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from myapp.models import ConferenceModel,TalkModel,MemberModel

MEMBER_CHOICES = [
    ("Speaker", "Speaker"),
    ("Participant", "Participant"),
]
class ConferenceForm(forms.ModelForm):
    class Meta:
        model = ConferenceModel
        fields = ['conference_title','conference_description','conference_start_date','conference_end_date']
        widgets = {
            'conference_title' : forms.TextInput(attrs={'class':'form-control '}),
            'conference_description' : forms.TextInput(attrs={'class':'form-control'}),
            'conference_start_date' : forms.TextInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),
            'conference_end_date' : forms.TextInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'})
        }

class TalkForm(forms.ModelForm):
    class Meta:
        model = TalkModel
        fields = ['talk_conference_title', 'talk_title', 'talk_description', 'room_number', 'projector_number', 'talk_duration', 'talk_time']
        widgets = {
            'talk_conference_title': forms.HiddenInput(),
            'talk_title': forms.TextInput(attrs={'class': 'form-control'}),
            'talk_description': forms.TextInput(attrs={'class': 'form-control'}),
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'projector_number': forms.TextInput(attrs={'class': 'form-control'}),
            'talk_duration': forms.TextInput(attrs={'class': 'form-control'}),
            'talk_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM:SS'}),
        }


class MemberForm(forms.ModelForm):
    member_type = forms.ChoiceField(choices=MEMBER_CHOICES,required=True)
    class Meta:
        model = MemberModel
        fields = ['member_type','member_talk_title','member_name','member_email']
        widgets = {
            'member_talk_title':forms.HiddenInput(),
            'member_name' : forms.TextInput(attrs={'class':'form-control '}),
            'member_email' : forms.TextInput(attrs={'class':'form-control '})
        }
