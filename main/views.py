from django.shortcuts import render
from .models import Brand
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.method == 'POST':
        search = request.POST['search']
        return render(request, 'index.html')
    brand = Brand.get_all_brand()
    return render(request,'index.html',{'brands' : brand})

def about(request):
    return render(request,'about.html')

def about(request):

    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def verificationmsg(request):
    return render(request,'verificationmsg.html')

def uploadmsg(request):
    return render(request,'uploadmsg.html')

def contactus(request):
    return render(request,'contactus.html')


def wtf(request):
    return render(request,'wtf.html')
@login_required(login_url='/account/login')
def codewtf(request):
    return render(request,'codeWtf.html')

def avni(request):
    return render(request,'avni.html')
@login_required(login_url='/account/login')
def codeavni(request):
    return render(request,'codeAvni.html')

def peesafe(request):
    return render(request,'PEESAFE.html')
@login_required(login_url='/account/login')
def codepeesafe(request):
    return render(request,'codePEESAFE.html')

def naagin(request):
    return render(request,'Naagin.html')
@login_required(login_url='/account/login')
def codenaagin(request):
    return render(request,'codeNaagin.html')

def tbh(request):
    return render(request,'TBH.html')
@login_required(login_url='/account/login')
def codetbh(request):
    return render(request,'codeTBH.html')

def propshop(request):
    return render(request,'propshop.html')
@login_required(login_url='/account/login')
def codepropshop(request):
    return render(request,'codePropshop.html')

def yesdone(request):
    return render(request,'YesDone.html')
@login_required(login_url='/account/login')
def codeyesdone(request):
    return render(request,'codeYesDone.html')

def unlu(request):
    return render(request,'unlu.html')
@login_required(login_url='/account/login')
def codeunlu(request):
    return render(request,'codeUnlu.html')

def unlu2(request):
    return render(request,'unlu2.html')
@login_required(login_url='/account/login')
def codeunlu2(request):
    return render(request,'codeUnlu2.html')

def trib(request):
    return render(request,'Trib.html')
@login_required(login_url='/account/login')
def codetrib(request):
    return render(request,'codeTrib.html')












