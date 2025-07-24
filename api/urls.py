from django.urls import path
from . import views

urlpatterns = [
    path('getemployees/',views.GetEmployee.as_view(),name='getemployeeurl'),
    path('updateemployee/<int:pk>/',views.UpdateEmployee.as_view())
]