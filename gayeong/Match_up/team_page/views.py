from django.shortcuts import render, redirect
from account.models import *

# Create your views here.
def teaminfo(request):
    return render(request, 'teaminfo.html')

def management(request):
    return render(request, 'management.html')

def testpage(request):
    return render(reqeust, 'testpage.html')