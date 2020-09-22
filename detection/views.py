from django.shortcuts import render, redirect
from .forms import StudentForm,Recordform 
from .models import Student, Records
from django.contrib import messages
from .filters import MyFilter
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime 
from dateutil import parser
from django.http.response import StreamingHttpResponse
import cv2
import face_recognition
import os
import numpy as np
from detection.camera import VideoCamera


# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

face_cascade = cv2.CascadeClassifier('C:/Users/bdn/Desktop/heyyy/Bdn/faceRec/detection/cascade/haarcascade_frontalface_default.xml')



def Student_list(request):
    # here if you want to displa only 4 records=== queryset=Student.objects.all()[:4]
      queryset=Student.objects.all()
      page = request.GET.get('page', 1)

      paginator = Paginator(queryset, 4)
      try:
        users = paginator.page(page)
      except PageNotAnInteger:
        users = paginator.page(1)
      except EmptyPage:
        users = paginator.page(paginator.num_pages)

      context ={
        "object_list":queryset,
        "page":page,
        "users":users
         
      }
      return render(request, "detection/student_list.html",context)
    # context = {'Student_list':Student.objects.all()}
    # return render(request,"detection/student_list.html",context)
    
def Student_form(request):
    if request.method == "GET":
        form = StudentForm()
        return render (request, "detection/student_form.html",{'form':form})
    else:
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # f ts true it wll redirect
            return redirect('/show')
       
        return render(request, 'detection/student_form.html', {'form': form})
        
def Student_delete(request):
    return render(request, "detection/student")

def Student_Record(request):
    return render(request, "detection/records")


def person_details(request, id):
    
    form = Student.objects.get(id=id)
    context = {
        'Student' : form
    }
    return render(request, 'detection/person_detail.html', context)


def search(request):
    if request.method == 'POST':
        srh = request.POST["srh"]
        if srh:
            match = Student.objects.filter(Q(id__contains=srh) )
            
            if match:
                return render(request,'detection/search.html', {'sr':match})
            else:
                messages.error(request,'no result found') 
        else:
                    return HttpResponseRedirect('/search')
    return render(request, 'detection/search.html')                

def Student_Attendance(request):
    if(request.method =="GET"):
        form = Recordform()
        return render(request, "detection/attendance.html", {'form':form})   
    else:
        form = Recordform(request.POST)
        if form.is_valid():
            form.save()
            # f ts true it wll redirect
            return redirect('/details')
       
        return render(request, 'ccc', {'form': form}) 
def Attendance_list(request):
    queryset=Records.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 4)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context ={
        "object_list":queryset,
        "page":page,
        "users":users
         
      }
    return render(request, "detection/recorddetail.html",context)

def datepicker(request):
    queryset=Records.objects.all()
    start_date = parser.parse(request.GET.get('start'))
    end_date = parser.parse(request.GET.get('end'))
    record = Records.objects.filter(Arrivedate__range =[ start_date, end_date])
    context ={
        "users":record
        }
    return render(request, "detection/returndate.html",context)

def attendanceRecord(request, id):
    # form = Records.objects.filter(student_id=id).order_by('-Arrivedate') 
    form = Records.objects.filter(student_id=id).order_by('-Arrivedate') 
    context = {
        'users' : form
    }
    return render(request, 'detection/AttendanceDetail.html', context)

#here am setting camera

# def detect_student(request):
#     if  request.method == 'POST':
#         cap = cv2.VideoCapture(0)
#         while True:
#             ret, frame = cap.read()
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             faces = face_cascade.detectMultiScale(gray, 1.5, 5)
#             for (x, y, w, h) in faces:
#                 cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
#             cv2.imshow('webcam', frame)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         cap.release()
#         cv2.destroyAllWindows()
#     return render(request, 'detection/detect_student.html')

# path = 'media/picture'
# tolerance = 0.2
# images = []
# classNames = []
# myFiles = os.listdir(path)
# # loop in this file to read image by image
# print(myFiles)

# for i in myFiles:
#     image = cv2.imread(f'{path}/{i}')
#     images.append(image)
#     classNames.append(os.path.splitext(i)[0])
# print(classNames)

# # we want to create a function to create uncodings of all images and put them in a list 

# def find_encodings(images):
#     list_encodings = []
#     for image in images:
#         encode = face_recognition.face_encodings(image)[0]
#         list_encodings.append(encode)
#     return list_encodings

# listofEncodings = find_encodings(images)
# print(listofEncodings[0])

# #here this is function to mark attendance to student whose camera saw

# def mark_attendance(name):
#     with open('Attendance.csv','r+') as f:
#         myFiles = f.readlines()
#         nameList = []
#         for line in myFiles:
#             entry = line.split(',')
#             nameList.append(entry[0])
#         if name not in nameList:
#             now = datetime.datetime.now()
#             dateString = now.strftime('%H:%M:%S')
#             f.writelines(f'\n{name},{dateString}')
# def detect_student(request):
#     if  request.method == 'POST':
#         cap = cv2.VideoCapture(0)
#         while True:
#             # Capture frame-by-frame
#             ret, image = cap.read()
#             # to speed up the process, we will resize the image captured 
#             image_small = cv2.resize(image, (0,0), None, 0.25, 0.25)
#             # convert the frame image to RGB
#             image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#             # create uncodings for our faces in the image 
#             # face_locations is now an array listing the co-ordinates of each face!
#             face_location = face_recognition.face_locations(image_small)
#             current_image_uncoding = face_recognition.face_encodings(image_small, face_location)
#             # find matches 
#             for encodeface, face_loc in zip(current_image_uncoding, face_location):
#                 matches = face_recognition.compare_faces(listofEncodings, encodeface)
#                 faceDist = face_recognition.face_distance(listofEncodings, encodeface) 
#                 print(faceDist)
#                 matchindex = np.argmin(faceDist)
#                 if matches[matchindex]:
#                     name = classNames[matchindex]
#             # print(name)
#                 y1,x2,y2,x1 = face_loc
#                 y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
#                 cv2.rectangle(image, (x1,y1), (x2,y2), (255,0,0), 2)
#                 cv2.rectangle(image, (x1,y2-20), (x2,y2), (255,0,0), cv2.FILLED)
#                 cv2.putText(image, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255), 2)
#             # here am calling the fuction to make attendance to known face viewed
#                 mark_attendance(name)
            
#                 cv2.imshow('frame',image)
            
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         cap.release()
#         cv2.destroyAllWindows()

#         # prince_image = face_recognition.load_image_file('media/images/Christian_Ronaldo.jpg')
#         # prince_test= face_recognition.load_image_file('media/images/sandesk.png')
#         # prince_image_encodings = face_recognition.face_encodings(prince_image)[0]
#         # prince_test_encodings = face_recognition.face_encodings(prince_test)[0]
#         # results = face_recognition.compare_faces([prince_image_encodings], prince_test_encodings)
#         # face_distance = face_recognition.face_distance([prince_image_encodings], prince_test_encodings)
#         # if results[0]:
#         #     print(f'The two faces matches at {face_distance}')
#         # else:
#         #     print(f'The two faces doesn\'t match at {face_distance}')

#     return render(request, 'detection/detect_student.html')

def index(request):
    return render(request, 'detection/home.html')    

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
