from dbapp.models import Employee,Deartment
from rest_framework import serializers

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['empname','empage','empsalary']
        
        