
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index),
    path('list/',views.employee_list,name='employee_list'),
    path('<int:id>/', views.update_form,name='employee_update'),
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('',views.employee_form,name='employee_insert'),
    
]

