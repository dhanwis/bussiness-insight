
from email import message
from django.shortcuts import  render
from django.core.mail import send_mail
from businesinsight import settings
from .forms import *
from django.conf import settings


from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')


