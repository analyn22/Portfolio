
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.conf import settings
from Portfolio.models import *
from Portfolio.forms import *
from django.contrib.auth import logout
from Anna.models import *

def home(request):
    prj = Projects.objects.all()
    designs = Design.objects.all()
    devlop = Developing.objects.all()
    det = External.objects.all()
    pers = Personal.objects.all()
    soc = Social.objects.all()
    if request.method == 'POST':
        form = Contact_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Send Successfully")
            return redirect('home')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = Contact_form()
    context = {
        'prj':prj,
        'designs':designs,
        'devlop':devlop,
        'det':det,
        'pers':pers,
        'form':form,
        'soc':soc,
        'jazzmin_settings': settings.JAZZMIN_SETTINGS,
    }
    return render(request,'index.html',context)

def project_description(request,slug):
    prj_details = get_object_or_404(Projects, slug=slug)
    context = {
        'prj_details':prj_details
    }
    return render(request,'description.html',context)

