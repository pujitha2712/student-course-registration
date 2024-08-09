from django.shortcuts import render, redirect
from .forms import StudentForm, CourseForm
from .models import Student, Course

def student_registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'registration/student_registration.html', {'form': form})

def course_registration(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'registration/course_registration.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'registration/student_list.html', {'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'registration/course_list.html', {'courses': courses})
