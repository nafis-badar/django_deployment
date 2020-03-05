from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def password(request):
    thepassword=""
    alpha=list("abcdefghijklmnopqrstuvwxyz")
    length=int(request.GET.get('length'))
    if request.GET.get("Uppercase"):
        alpha.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("Numbers"):
        alpha.extend(list("1234567890"))
    if request.GET.get("Special"):
        alpha.extend(list("!@#$%^&*()"))

    for x in range(length):
        thepassword+=random.choice(alpha)

    return render(request,'password.html',{'password':thepassword})
