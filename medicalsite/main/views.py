from django.shortcuts import render
from django.shortcuts import HttpResponse,render,HttpResponseRedirect,redirect,reverse
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.contrib.auth import authenticate,logout
import json
from .forms import AdminRegistrationForm
from .models import Medical_entries
from django.contrib import messages
from django.utils.timezone import localdate
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from urllib.parse import urlparse
from urllib.parse import parse_qs
from django.forms import ModelForm


def register(request):
    return render(request=request, template_name='register.html')

def register_user(request):
    if request.POST:

        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        pw = request.POST.get('pw')
        pw_confirm = request.POST.get('pw_confirm')

        aadhar_no=request.POST.get('aadhar_no')

        user = User()
        user.first_name = f_name
        user.last_name = l_name
        user.username = email
        user.aadhar_no = aadhar_no

        if pw == pw_confirm:
            user.set_password(pw)
        else:
            return HttpResponse(json.dumps([{"validation": "Password does not match", "status": False}]),
                                content_type="application/json")
        user.is_staff = True
        user.save()
        register_success = [{"validation": "Registration Successful", "status": True}]
        return HttpResponse(json.dumps(register_success), content_type="application/json")
    else:
        return HttpResponse(json.dumps([{"validation": "I am watching you (0_0)", "status": False}]),
                            content_type="application/json")

def login(request):
    if request.POST:
        email = request.POST.get('email')
        pw = request.POST.get('pw')
        log_user = authenticate(username=email, password=pw)
        if log_user is not None:
            authentication_success = [{"validation": "Authentication Successful", "status": True}]
           
            request.session['cur_user'] = log_user.first_name
            request.session['username'] = log_user.username
            request.session.save()
            return redirect('dashboard')
       
        else:
           messages.info(request, 'Not valid credentials')
           return redirect(reverse('register'))


def dashboard(request):
   medical_entries=Medical_entries.objects.values().filter(email=request.session['username'])
   return render(request,'dashboard.html',{"name":request.session['cur_user'],"email":request.session['username']})

def logout_request(request):
    logout(request)
    return redirect(reverse('register'))

def med_create(request):
   return render(request,'newMed.html',{"name":request.session['cur_user']})

def getMedData(request):
    medData=list(Medical_entries.objects.values().filter(email=request.session['username']))
    content=JSONRenderer().render(medData)
    return HttpResponse(content,content_type="application/json")

def add_med(request):
    title=request.POST.get('title')
    email=request.session['username']
    description=request.POST.get('desc')

    posted_on=localdate()
   
    med=Medical_entries(title=title,description=description,email=email,posted_on=posted_on)
    med.save()    
    messages.info(request, "Condition registered")
    return redirect('dashboard')    

@csrf_exempt
def my_Med(request):
    med_id=urlparse(str(request))
    med_id=parse_qs(med_id.query)['id'][0]
    med_id=med_id[:-2]
    id,button=med_id.split('_')
        
    if button=="view":
        med=Medical_entries.objects.values().filter(med_id=id)[0]['med_id']
        request.session['med']=med
        request.session['id']=id
        return redirect('view')

    if button=="remove":
        med=Medical_entries.objects.values().filter(med_id=id)[0]['med_id']
        request.session['med']=med
        request.session['id']=id
        return redirect('remove')

    return redirect('dashboard')
def remove(request):
    id=request.session['med']
    med=Medical_entries.objects.filter(med_id=id)
    #print(job)
    med.delete()
    return redirect('dashboard')

def view(request):
    med=Medical_entries.objects.values().filter(med_id=request.session['med'])
    return render(request,'MedDetails.html',{'id':request.session['id'],'title':med[0]['title'],'name':request.session['cur_user'],"description":med[0]['description']})
