from django.shortcuts import render
from django.views import View
from .models import Deartment,Employee

# Create your views here.

class InsertEmployee(View):
    def get(self,req):
        depts = Deartment.objects.all()
        return render(req,'dbapp/insert.html',{'depts':depts})
    
    def post(self,req):
        print(req.POST)
        ename = req.POST['ename']
        eage = req.POST['eage']
        esal = req.POST['esal']
        deptno = req.POST['dept']
        dept_details = Deartment.objects.get(deptid = deptno)
        Employee.objects.create(empname = ename,empage = eage,empsalary = esal,empdepartment = dept_details)
        return render(req,'dbapp/insert.html')
    
    
class SelectEmployee(View):
    def get(self,req):
        emps = Employee.objects.all()
        return render(req,'dbapp/select.html')