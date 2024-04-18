from django.db import models
from django.utils import timezone

MEMBER_CHOICES = [
    ("Speaker", "Speaker"),
    ("Participant", "Participant"),
]

class ConferenceModel(models.Model):
    conference_title = models.TextField(primary_key=True)
    conference_description = models.CharField(max_length=1000)
    conference_start_date = models.DateField()
    conference_end_date = models.DateField()

class TalkModel(models.Model):
    talk_conference_title = models.ForeignKey(ConferenceModel, on_delete=models.CASCADE)
    talk_title = models.TextField(primary_key=True)
    talk_description = models.CharField(max_length=100)
    room_number = models.CharField(max_length=20)  # Add room number field
    projector_number = models.CharField(max_length=20)  # Add projector number field
    talk_duration = models.DecimalField(max_digits=3, decimal_places=1)  # Adjusted max_digits
    talk_time = models.TimeField(null=True)
    
class MemberModel(models.Model):
    member_talk_title = models.ForeignKey(TalkModel, on_delete=models.CASCADE)
    member_type = models.CharField(max_length=25, choices=MEMBER_CHOICES)
    member_name = models.TextField(primary_key=True)
    member_email = models.EmailField(max_length=100, unique=True)
