from django.db import models

# Create your models here.

class Deartment(models.Model):
    deptid = models.AutoField(primary_key=True)
    deptname = models.CharField(max_length=25)
    deptloc = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.deptname




class Employee(models.Model):
    empid = models.AutoField(primary_key=True)
    empname = models.CharField(max_length=30)
    empage = models.IntegerField()
    empsalary = models.IntegerField()
    empdepartment = models.ForeignKey(Deartment,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.empname