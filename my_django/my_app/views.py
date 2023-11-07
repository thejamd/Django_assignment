from django.shortcuts import render
from django.http import HttpResponse
# def my(request):
#     return HttpResponse("<b>This is My Page</b>")
def printhello(request):
    student_data={
    'student':[
        {'name':"theja",
         'course':"python",
         'mark':50,
         'status':True},
         {'name':"sneha",
         'mark':40,
         'course':"python",
         'status':True},
         {'name':"anjali",
         'mark':55,
         'course':"",
         'status':True},
         {'name':"aleena",
         'mark':48,
         'course':"python",
         'status':True}]}
    return render(request, 'index.html',student_data)
# Create your views here.
