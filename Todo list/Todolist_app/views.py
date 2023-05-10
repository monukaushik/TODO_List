from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from datetime import datetime

def index(request):
    data=todo.objects.all()
    return render(request,'index.html',{'data':data})

def task_detail(request):
    if request.method != 'POST':
        return render(request,'task_detail.html')
    t=todo()
    t.task=request.POST.get('task')
    t.start_time=request.POST.get('stime')
    t.end_time=request.POST.get('etime')
    t.date=request.POST.get('date')
    t.status=request.POST.get('status')
    t.save()
    return redirect('/')

def update(request,id):
    data1=todo.objects.filter(id=id).first()
    task=data1.task
    start_time = data1.start_time.strftime("%H:%M") 
    end_time = data1.end_time.strftime("%H:%M") 
    date = data1.date.strftime("%Y-%m-%d") 
    status=data1.status
 
    context={
        'task':task,
        'start_time':start_time,    
        'end_time':end_time,
        'date':date,
        'status':status,
    }

    if request.method=='POST':
        data1.task=request.POST.get('task')
        data1.start_time=request.POST.get('stime')
        data1.end_time=request.POST.get('etime')
        data1.date=request.POST.get('date')
        data1.status=request.POST.get('status')
        data1.save()
        return redirect('/')
    return render(request,'update.html',context)

def delete(request,id):
    data1=todo.objects.get(id=id)
    data1.delete()
    return HttpResponseRedirect('/')

