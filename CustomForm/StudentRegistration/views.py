from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import enroll
from .models import enrollDB

# Create your views here.

def register(request):
    if request.method == 'POST':
        register = enroll(request.POST)
        if register.is_valid():
            #register = register.cleaned_data
            f_name = register.cleaned_data['first_name']
            l_name = register.cleaned_data['last_name']
            em = register.cleaned_data['email']
            pw = register.cleaned_data['password']
            rpw = register.cleaned_data['rpassword']
            saveData = enrollDB(first_name = f_name, last_name = l_name, email = em, password = pw, rpassword = rpw)
            saveData.save()
            return HttpResponseRedirect('/success/')
            # return render(request,'success.html',{'name':name})
    else:
        register = enroll()
    return render(request, "registration.html",{'register' : register})

def thankyou(request):
    return render(request,'success.html')
