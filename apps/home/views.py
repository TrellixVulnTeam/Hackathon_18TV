# -*- encoding: utf-8 -*-

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.home.models import Profile, Diseases



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def profile(request):
    if request.method == 'POST':
        b = request.user
        try:
            a = Profile.objects.get(id = b.id)
            a.username=request.POST.get('username')
            a.email=request.POST.get('email')
            a.firstname=request.POST.get('firstname')
            a.lastname=request.POST.get('lastname')
            a.address=request.POST.get('address')
            a.city=request.POST.get('city')
            a.country=request.POST.get('country')
            a.zip=request.POST.get('zip')
            a.age=request.POST.get('age')
            a.disease=request.POST.get('disease')
            a.save()
            messages.success(request,'Profile Updated Successfully')
            return render(request,'home/profile.html',{'a':a})
        except Profile.DoesNotExist:
            saverecord=Profile()
            saverecord.username=request.POST.get('username')
            saverecord.email=request.POST.get('email')
            saverecord.firstname=request.POST.get('firstname')
            saverecord.lastname=request.POST.get('lastname')
            saverecord.address=request.POST.get('address')
            saverecord.city=request.POST.get('city')
            saverecord.country=request.POST.get('country')
            saverecord.zip=request.POST.get('zip')
            saverecord.age=request.POST.get('age')
            saverecord.disease=request.POST.get('disease')
            messages.success(request,'Profile Recorded Successfully')
            saverecord.save()
            b = request.user
            try:
                a = Profile.objects.get(id = b.id)
            except Profile.DoesNotExist:
                a=None
            return render(request,'home/profile.html',{'a':a})
    else:
        b = request.user
        try:
            a = Profile.objects.get(id = b.id)
        except Profile.DoesNotExist:
            a=None
        return render(request,'home/profile.html',{'a':a})

@login_required(login_url="/login/")
def tests(request):
    if request.method =="POST":
        agegrp = request.POST.get('agegrp')
        sleep = request.POST.get('sleep')
        weight = request.POST.get('weight')
        places1 = request.POST.get('places1')
        places2 = request.POST.get('places2')
        disorders = request.POST.get('disorders')
        if agegrp =="less10":
            predict ="Be With your phone less 😊"
        elif agegrp!="less10" and (sleep!='8' or sleep!='less6') and weight=="over":
            predict= "You have obesity caused be sleeping disorder"

        elif agegrp!="less10" and (sleep!='8' or sleep!='less6') and weight=="under":
            predict="You have weightloss problem caused be sleeping disorder"
        
        elif agegrp!="less10" and weight=="under" and places1=="lowerabdomen" and places2=="stomach":
            predict="You might have period cramps if not visit a gynacologist"
        
        elif agegrp!="less10" and weight=="under" and places1=="stomach" and places2=="lowerabdomen":
            predict= "You might have period cramps if not visit a gynacologist"
        
        elif agegrp!="less10" and weight=="over" and places1=="lowerabdomen" and places2=="stomach":
            predict= "You might have period cramps if not visit a gynacologist"
        
        elif agegrp!="less10" and weight=="over" and places1=="stomach" and places2=="lowerabdomen":
            predict= "You might have period cramps if not visit a gynacologist"
        
        elif agegrp!="less10" and (sleep!='8' or sleep!='less6') and weight=="normal" and (places1=="chest" or places2=="chest") and disorders=="breathlessness":
            predict = "You might have anxiety issues"
        
        elif agegrp!="less10" and (sleep!='8' or sleep!='less6') and weight=="normal":
            predict = "You may have sleeping disorder"
    
        return render(request,'home/tests.html',{'predict':predict})
    return render(request,'home/tests.html')


@login_required(login_url="/login/")
def diets(request):
    return render(request,'home/diets.html')

def first(request):
    return render(request,'home/firstpg.html')

def searched(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        if searched=="Allegry" or searched=="allergies" or searched=="allergy" or searched=="Allergies":
            return render(request,"diseases/allergy.html")
        elif searched=="Bronchitis" or searched=="bronchitis":
            return render(request, "diseases/brochitis.html")
        elif searched=="Anxiety" or searched=="anxiety":
            return render(request, "diseases/anxiety.html")
        else:
            return HttpResponse("Sorry We dont have that information :(")


        '''diseases = Diseases.objects.filter(name__contains=searched)
        diseases.name=request.POST.get('name')
        diseases.description=request.POST.get('description')
        diseases.symptom=request.POST.get('symptom')
        diseases.precautions=request.POST.get('precaution')
        diseases.cure=request.POST.get('cure')
        return render(request,'home/searched.html',{'searched':searched,'diseases':diseases})'''
    else:
        return render(request,'home/searched.html',{})
def hair(request):
    return render(request,'home/hairloss.html')

def weight(request):
    return render(request,'home/weight.html')

def skin(request):
    return render(request,'home/skin.html')

def nutrition(request):
    return render(request,'home/nutrition.html')
def depression(request):
    return render(request,'home/depression.html')
def sleepdisorders(request):
    return render(request,'home/sleepdisorders.html')
def weightmanagement(request):
    return render(request,'home/weightmanagement.html')
def workholic(request):
    return render(request,'home/workholic.html')