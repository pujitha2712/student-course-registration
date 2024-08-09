from django.urls import path
from . import views

urlpatterns = [
    path('register/student/', views.student_registration, name='student_registration'),
    path('register/course/', views.course_registration, name='course_registration'),
    path('students/', views.student_list, name='student_list'),
    path('courses/', views.course_list, name='course_list'),
]
