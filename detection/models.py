from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save

# Create your models here.
class Student(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True, auto_created=False, max_length=10000)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField('date of birth')
    departement = models.CharField(max_length=200)
    gender_choices = (
        ("M", "MALE"),
        ("F", "FEMALE")
    )
    gender = models.CharField(max_length=1,  choices=gender_choices)
    status_choices = (
        (0, "BLOCKED"),
        (1, "ALLOWED")
    )
    status = models.IntegerField(max_length=1, choices=status_choices)
    reason = models.CharField(max_length=200, blank=True, null=True, default=None)
    photoUrl = models.ImageField(upload_to='picture')

    def __str__(self):
        return self.first_name
    
class Records(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Arrivedate = models.DateTimeField("Arriving Date")
    campus_choices = (
        ("G", "GISHUSHU CAMPUS"),
        ("M", "MASORO CAMPUS")
    )
    campus = models.CharField(max_length=100, choices=campus_choices) 

def __str__(self):
       return self.campus