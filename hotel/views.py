from django.shortcuts import render
from .models import Register
from .models import Messages
# Create your views here.
def home(request):
    return render(request,'hotel/index.html')

def contact(request):
    if request.method=="GET":
        return render(request,'hotel/contact.html')
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phn=request.POST['phone']
        msg=request.POST['msg']
        x=Messages(name=name,email=email,phone=phn,message=msg)
        x.save()
        dictionary={
            'msg':"Your Message Is Shared"
        }
        return render(request,'hotel/contact.html',context=dictionary)
def map(request):
    if (request.method=='GET'):
        return render(request,'hotel/map.html')

def register(request):
    if request.method=="GET":
        return render(request,'hotel/register.html')
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pswd']
        cp=request.POST['cp']
        if password==cp:
            e=Register(name=name,email=email,password=password)
            e.save()
            dictionary={
                'msg1':"Registered Successfully"
            }
            return render(request,'hotel/register.html',context=dictionary)
        else:
            dictionary={
                'msg2':"Passwords didn't match"
            }
            return render(request,'hotel/register.html',context=dictionary)


def login(request):
    if request.method=="GET":
        return render(request,'hotel/login.html')
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        e=Register.objects.raw('select * from hotel_register where email="'+str(email) +'" and password="'+str(password)+'"')
        if len(e)>0:
            return render(request,'hotel/rooms.html')
        else:
            dictionary={
                'msg':"Invalid Credentials!!!"
            }
            return render(request,'hotel/login.html',context=dictionary)

def list_page(request):
    if request.method=="GET":
        return render(request,'hotel/list.html')

