# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf import settings
from django.utils import timezone
#import mammoth
from django.shortcuts import render
from django.core.mail import send_mail
import random
from .forms import ContactForm
from .models import Contact, Carrers



from django.shortcuts import render

# Create your views here.
def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        firstname = form.cleaned_data['firstname']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        create = Contact.objects.get_or_create(firstname=firstname, email=email, message=message)
        subject='Thankyou for contacting us'
        email_message='we get in few moments'
        From_mail=settings.EMAIL_HOST_USER
        to_list=[email,settings.EMAIL_HOST_USER]
        send_mail(subject,email_message,From_mail,to_list,fail_silently=True)


    template='index.html'
    context={

    }
    return render(request,template,context)

def  jobs(request):
    list_filter = ['time']
    now = timezone.now()

    order_by = Carrers.objects.order_by('-id')

    template = "careers.html"
    context = {'order': order_by,'id':id
               }
    return render(request,template,context)


def ourprojects(request):
    template='ourprojects.html'
    context={
    }
    return render(request,template,context)

def dammi(request):
    template='dammi.html'
    context={

    }
    return render(request,template,context)