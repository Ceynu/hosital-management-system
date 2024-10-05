from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors list',views.doctor_list,name='doctors list'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book_appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('appointment_history/', views.appointment_history, name='appointment_history'),
]

