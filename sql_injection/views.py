from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render

from .models import *


@require_GET
def home(request: HttpRequest):
    return render(request, 'sql_injection/index.html')


@require_GET
def sqli_vulnerable_get_students(request: HttpRequest):
    if request.GET.get('first_name'):
        raw_queryset = Student.objects.raw(
            f'SELECT * FROM sql_injection_student WHERE first_name = "{request.GET["first_name"]}"'
        )
    else:
        raw_queryset = Student.objects.raw(
            f'SELECT * FROM sql_injection_student'
        )
    return render(request, 'sql_injection/students.html', {'students': raw_queryset})


@require_GET
def sqli_protected_get_students(request: HttpRequest):
    queryset = Student.objects.all()
    if request.GET.get('first_name'):
        queryset = queryset.filter(first_name=request.GET['first_name'])
    return render(request, 'sql_injection/students.html', {'students': queryset})