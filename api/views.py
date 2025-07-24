from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from dbapp.models import Employee,Deartment
from .serializers import EmpSerializer
# Create your views here.


# api_view(['GET','POST'])
class GetEmployee(APIView):
    def get(self,req):
        emps = Employee.objects.all()
        seri_obj = EmpSerializer(emps,many = True)
        return Response(seri_obj.data,status=HTTP_200_OK)
    
    def post(self,req):
        seri_obj = EmpSerializer(data = req.data)
        if seri_obj.is_valid():
            seri_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(seri_obj.errors,status=HTTP_400_BAD_REQUEST)
            
        
# @api_view(['GET','DELETE','PUT'])       
class UpdateEmployee(APIView):
    def get(self,req,pk):
        emp = Employee.objects.get(empid = pk)
        seri_obj = EmpSerializer(emp)
        return Response(seri_obj.data,status=HTTP_200_OK)
    
    def put(self,req,pk):
        emp = Employee.objects.get(empid = pk)
        seri_obj = EmpSerializer(emp, data = req.data)
        if seri_obj.is_valid():
            seri_obj.save()
            return Response(seri_obj.data,status=HTTP_200_OK)
        else:
            return Response(seri_obj.errors,status=HTTP_400_BAD_REQUEST)
        
    def delete(self,req,pk):
        emp = Employee.objects.get(empid = pk)
        emp.delete()
        
    