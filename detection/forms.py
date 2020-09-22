from django import forms
from .models import Student
from .models import Records

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

class Recordform(forms.ModelForm):

    class Meta:
        model = Records
        fields = '__all__'