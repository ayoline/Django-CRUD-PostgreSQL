from django.shortcuts import render
from CRUDOperation.models import EmpModel
from CRUDOperation.forms import Empforms
from django.contrib import messages

def showemp(request):
    showall = EmpModel.objects.all()
    return render(request,'Index.html',{"data":showall})

def Insertemp(request):
    if request.method=="POST":
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('occupation') and request.POST.get('salary') and request.POST.get('gender'):
            saverecord =  EmpModel()
            saverecord.empname = request.POST.get('empname')
            saverecord.email = request.POST.get('email')
            saverecord.occupation = request.POST.get('occupation')
            saverecord.salary = request.POST.get('salary')
            saverecord.gender = request.POST.get('gender')
            saverecord.save()
            messages.success(request, 'Employee ' + saverecord.empname + ' is saved successfully!')
            return render(request, 'Insert.html')
    else:
        return render(request, 'Insert.html')

def Editemp(request, id):
    editempobj = EmpModel.objects.get(id=id)
    return render(request, 'Edit.html', {"EmpModel":editempobj})

def Updateemp(request, id):
    Updateemp = EmpModel.objects.get(id=id)
    form = Empforms(request.POST, instance=Updateemp)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record updated successfully!')
        return render(request, 'Edit.html', {"EmpModel":Updateemp})

def Delemp(request,id):
    delemployee = EmpModel.objects.get(id=id)
    delemployee.delete()
    showdata = EmpModel.objects.all()
    return render(request, "Index.html", {"data":showdata})