from django.urls import path
from .views import *

app_name = 'sql_injection'
urlpatterns = [
    path('', home, name='home'),
    path('vulnerable/get-students/', sqli_vulnerable_get_students, name='get-students-vulnerable'),
    path('protected/get-students/', sqli_protected_get_students, name='get-students-protected'),
]