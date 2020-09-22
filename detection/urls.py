from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('video_feed', views.video_feed, name="video_feed"),
    path('addStudent', views.Student_form,name='add_student'),
    path('show/', views.Student_list),
    path('details/<int:id>',views.person_details),
    path('search/',views.search),
    path('attendance/', views.Student_Attendance),
    path('details/', views.Attendance_list),
    path('details/datepicker/',views.datepicker),
    path('personRecord/<int:id>',views.attendanceRecord),
    # path('detection', views.detect_student, name='webcamdetection'),
   
]
