from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def index(request):
    return render(request,'base.html')

def employee_list(request): 
    if 'q' in request.GET:
        q=request.GET['q']
        context={'employee_list':Employee.objects.filter(Name__icontains=q)}
    else:
        # posts=Post.objects.all()
        context = {'employee_list':Employee.objects.all()}
        # return render(request,'employee_list.html',context) 
    return render(request,'employee_list.html',context)  

def employee_form(request,id=0):
    if request.method =="GET": 
        form = EmployeeForm()
        return render(request,'employee_form.html',{'form':form})   
    else:
        form = EmployeeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/list')
        
def update_form(request,id):
    if request.method =="GET": 
        employee = Employee.objects.get(pk=id)
        form=EmployeeForm(instance=employee)
        return render(request,'employee_form.html',{'form':form})   
    else:
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST,instance= employee)
        
    if form.is_valid():
            form.save()
            return redirect('/list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')           