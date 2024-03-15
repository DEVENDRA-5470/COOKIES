from django.http import HttpResponse
from django.shortcuts import render
from main.imports import *
from main.forms import *
from datetime import datetime , timedelta

# Create your views here.
def user_sign(request):
    if request.method == 'POST':
        form = sign_form(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponse('done')
        else:
            print(form.errors)
    form = sign_form()
    args = {'form' : form}
    return render(request, 'sign_login.html',args)


def setcookie(request):
    re=render(request ,'home.html')
    re.set_cookie('name',"devendra Python")
    return re
def setcookie1(request):
    re=render(request ,'home.html')
    # re.set_cookie('name',"devendra Python djnago",max_age=30)
    re.set_cookie('name',"devendra Python djnago",expires=datetime.utcnow()+timedelta(days=2))
    return re
def getcookie1(request):
    # data=request.COOKIES['name']
    data=request.COOKIES.get('name')
    return render(request,'get.html',{'data':data})
def delcookie1(request):
    re=render(request ,'home.html')
    re.delete_cookie('name')
    return re
    
   