from django.contrib import admin
from myapp.models import ConferenceModel,TalkModel,MemberModel

admin.site.register(ConferenceModel)
admin.site.register(TalkModel)
admin.site.register(MemberModel)
# Register your models here.
