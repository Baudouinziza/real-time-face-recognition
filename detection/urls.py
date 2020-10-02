from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('video_feed', views.video_feed, name="video_feed"),
    path('addStudent', views.Student_form,name='add_student'),
    path('show/', views.Student_list,name="StudentRecords"),
    path('person_details/<int:id>',views.person_details),
    path('search/',views.search),
    path('attendance/', views.Student_Attendance),
    path('details/', views.Attendance_list),
    path('details/datepicker/',views.datepicker),
    path('personRecord/<int:id>',views.attendanceRecord),
    # 2
    path('create_dataset', views.create_dataset),
    path('trainer', views.trainer),
    path('detect', views.detect),
    # send email
    path('email', views.email),

]
