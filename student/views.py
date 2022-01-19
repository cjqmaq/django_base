from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.urls import reverse

from student.models import Student

def add_page(req):
    return render(req,'student/add.html')

def add_save(req):
    student = Student()
    student.student_code = req.POST['student_code']
    student.name = req.POST['name']
    student.sex = req.POST['sex']
    student.grade = req.POST['grade']
    student.marjo = req.POST['marjo']
    student.save()
    return HttpResponseRedirect(reverse('student:index'))
def index(req):
    students_list = Student.objects.all()
    return  render(req,'student/index.html',{'students_list':students_list})

def edit(req,students_id):
    students = get_object_or_404(Student, pk=students_id)
    return  render(req,'student/edit.html',{'students':students})

def edit_save(req):
    students_list = get_object_or_404(Student,pk=req.POST['students_id'])
    students_list.student_code = req.POST['student_code']
    students_list.name = req.POST['name']
    students_list.sex = req.POST['sex']
    students_list.grade = req.POST['grade']
    students_list.marjo = req.POST['marjo']
    students_list.save()
    return HttpResponseRedirect(reverse('student:index'))
    # students_list1 = Student.objects.all()
    # return render(req,'student/index.html',{'students_list':students_list1})

def delet_students(req,students_id):
     students_list = get_object_or_404(Student,pk=students_id)
     students_list.delete()
     return HttpResponseRedirect(reverse('student:index'))


