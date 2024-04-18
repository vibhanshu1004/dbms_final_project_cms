from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponsePermanentRedirect,HttpResponse
from myapp.forms import ConferenceForm,TalkForm,MemberForm
from myapp.models import ConferenceModel,TalkModel,MemberModel
# Create your views here.

def home(request):
    return render(request, "indexx.html")
def conferenceView(request):
    if request.method == 'POST':
        conferenceform = ConferenceForm(request.POST)
        if conferenceform.is_valid():
            conferenceform.save()
            conferenceform = ConferenceForm()  
    else:
        conferenceform = ConferenceForm()
    conference = ConferenceModel.objects.all()
    return render(request,'myapp/conference.html',{'conference':conference,'conferenceform':conferenceform})

def conferenceedit(request,id):
    if request.method == 'POST':
        uniqueconferencetitle = ConferenceModel.objects.get(pk=id)
        requestconferencedetails = ConferenceForm(request.POST,instance=uniqueconferencetitle)
        if requestconferencedetails.is_valid():
            requestconferencedetails.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))
    else:
        uniqueconferencetitle = ConferenceModel.objects.get(pk=id)
        requestconferencedetails = ConferenceForm(instance=uniqueconferencetitle)
    return render(request,'myapp/conferenceedit.html',{'requestconferencedetails':requestconferencedetails})
    

def conferencedelete(request,id):
    if request.method == 'POST':
        conferencedelete = ConferenceModel.objects.get(pk=id)
        conferencedelete.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))

def talkView(request,id):
    initial = {'talk_conference_title':id}
    if request.method == 'POST':
        talkviewform = TalkForm(request.POST)
        if talkviewform.is_valid():
            talkviewform.save()
        
    else:
        talkviewform=TalkForm(initial=initial)

    talk = ConferenceModel.objects.get(pk=id)
    conferencetalks = talk.talkmodel_set.all()
    return render(request,'myapp/talks.html',{'talkviewform':talkviewform,'conferencetalks':conferencetalks})


def talkdelete(request,id):
    if request.method == 'POST':
        talkdelete = TalkModel.objects.get(pk=id)
        talkdelete.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))

def talkedit(request,id):
    if request.method == 'POST':
        uniquetalktitle = TalkModel.objects.get(pk=id)
        requesttalkdetails = TalkForm(request.POST,instance=uniquetalktitle)
        if requesttalkdetails.is_valid():
            requesttalkdetails.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))
    else:
        uniquetalktitle = TalkModel.objects.get(pk=id)
        requesttalkdetails = TalkForm(instance=uniquetalktitle)
    return render(request,'myapp/talkedit.html',{'requesttalkdetails':requesttalkdetails})

def memberView(request,id):
    initial = {'member_talk_title':id}
    if request.method == 'POST':
        memberviewform = MemberForm(request.POST)
        if memberviewform.is_valid():
            memberviewform.save()
        
    else:
        memberviewform=MemberForm(initial=initial)
    member = TalkModel.objects.get(pk=id)
    allthemembers = member.membermodel_set.all()
    return render(request,'myapp/member.html',{'allthemembers':allthemembers,'memberviewform':memberviewform})

def memberDelete(request,id):
    if request.method == 'POST':
        deletemember = MemberModel.objects.get(pk=id)
        deletemember.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))