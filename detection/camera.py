import cv2, os, urllib.request,requests
import numpy as np
from django.conf import settings
import  face_recognition 
import datetime 
from dateutil import parser
from detection.models import Student
from django.shortcuts import redirect

ids = []
classNames = []
tolerance = 0.2
students = Student.objects.values('id','last_name', 'photoUrl')
print('---------------------------------------------------')
print(students)
# names = []
images = []
print('Hello +++++++++++++++++++++++ ')
for student in students:
    classNames.append(str(student['id'])) 
    image = face_recognition.load_image_file('media/'+student['photoUrl'])   
    images.append(image)
# print(images[0])

# path = 'media/picture'
# images = []
# myFiles = os.listdir(path)
# # loop in this file to read image by image
# print(myFiles)

# for i in myFiles:
#     image = cv2.imread(f'{path}/{i}')
#     images.append(image)
#     classNames.append(os.path.splitext(i)[0])
# print(classNames)

# we want to create a function to create uncodings of all images and put them in a list 

def find_encodings(images):
    list_encodings = []
    for image in images:
        face_loc = face_recognition.face_locations(image)
        encode = face_recognition.face_encodings(image, face_loc)[0]
        list_encodings.append(encode)
    return list_encodings
listofEncodings = find_encodings(images)
# print(listofEncodings[0])
 # #here this is function to mark attendance to student whose camera saw
    
def mark_attendance(name):
    with open('Attendance.csv','r+') as f:
        myFiles = f.readlines()
        nameList = []
        for line in myFiles:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.datetime.now()
            dateString = now.strftime('%Y-%m-%d %H:%M:%S')
            f.writelines(f'\n{name},{dateString}')
def mark_id(name):
                return redirect('/show/')

class VideoCamera(object):
    #here am setting camera
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        # (self.grabbed, self.frame) = self.video.read()
        # threading.Thread(target=self.update, args=()).start()
    def get_frame(self):
        success, image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        images_resize = cv2.resize(image, (0,0), None, 0.25, 0.25)
         # create uncodings for our faces in the image 
         # face_locations is now an array listing the co-ordinates of each face!
        face_locations = face_recognition.face_locations(images_resize)
        current_image_encodings = face_recognition.face_encodings(images_resize, face_locations)
        for encodeface, faceloc, in zip(current_image_encodings, face_locations):
            matches = face_recognition.compare_faces(listofEncodings, encodeface)
            faceDist =face_recognition.face_distance(listofEncodings, encodeface)
            print(faceDist) 
           # find matches 
            name = 'Unknown'
            matchindex = np.argmin(faceDist)
            if matches[matchindex]:
                name= classNames[matchindex]
            y1,x2,y2,x1 = faceloc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(image, (x1,y1), (x2,y2), (255,0,0), 2)
            cv2.rectangle(image, (x1,y2-20), (x2,y2), (255,0,0), cv2.FILLED)               
            cv2.putText(image, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255), 2)
            mark_id(name)
# here am calling the fuction to make attendance to known face viewed
            mark_attendance(name)
        # faces_detected = face_datection.detectMultiScale(gray, 1.5, 5)
        # for(x, y, w, h) in faces_detected:
        #     cv2.rectangle(image, (x,y), (x+w, y+h), (0, 0, 255), 2)
        frame_flip = cv2.flip(image,1)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


    def __del__(self):
        self.video.release()


     