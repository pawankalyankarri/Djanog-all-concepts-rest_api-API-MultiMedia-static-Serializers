from django.urls import path
from . import views

urlpatterns = [
    path('insert/',views.InsertEmployee.as_view(),name='inserturl'),
    path('select/',views.SelectEmployee.as_view(),name='selecturl')
]