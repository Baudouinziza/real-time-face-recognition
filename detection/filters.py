import django_filters
from .models import *




class MyFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = 'id','first_name','last_name'

