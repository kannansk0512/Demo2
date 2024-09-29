from django.shortcuts import render,redirect
from .models import mobiles



def index(request):
    return render(request,'index.html')


def add(request):
    if request.method=='POST':
        dt=mobiles()
        dt.brand=request.POST.get('brand')
        dt.model=request.POST.get('model')
        dt.colour=request.POST.get('color')
        dt.price=request.POST.get('price')
        dt.save()
        return redirect('/')
    return render(request,'add.html')


def show(request):
    dt=mobiles.objects.all()
    return render(request,'view.html',{'data':dt})


def edit(request,id):
    dt=mobiles.objects.get(id=id)
    if request.method=='POST':
        dt.brand=request.POST.get('brand')
        dt.model=request.POST.get('model')
        dt.colour=request.POST.get('color')
        dt.price=request.POST.get('price')
        dt.save()
        return redirect('/view/')
    return render(request,'edit.html',{'data':dt})


def delet(request,id):
    dt=mobiles.objects.get(id=id)
    dt.delete()
    return redirect('/view/')

def demo(request):
    a= request.COOKIES
    print(a)
    count=request.COOKIES.get('my')
    print(count)
    if count:
        count=int(count)+1
    else:
        count=1
    c= render(request,'demo.html',{'count':count})
    c.set_cookie('my',count)
    return c


