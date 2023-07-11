import cv2
import uuid
import face_recognition

import sys
from os import path
import numpy as np
import subprocess

import pyttsx3
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
#test_image = cv2.imread('image_zoomed.png')

face_dict = {}


#encoding faces
bilel_img = face_recognition.load_image_file("bilel.png")
bilel_encoding = face_recognition.face_encodings(bilel_img)[0]

ayoub_img = face_recognition.load_image_file("ayoub.png")
ayoub_encoding = face_recognition.face_encodings(ayoub_img)[0]

arbi_img = face_recognition.load_image_file("arbi.png")
arbi_encoding = face_recognition.face_encodings(arbi_img)[0]

ali_img = face_recognition.load_image_file("Ali.png")
ali_encoding = face_recognition.face_encodings(ali_img)[0]

farah_img = face_recognition.load_image_file("farah.png")
farah_encoding = face_recognition.face_encodings(farah_img)[0]

# ahdi_img = face_recognition.load_image_file("Ahdi.png")
# ahdi_encoding = face_recognition.face_encodings(ahdi_img)[0]

known_face_encoding = [
bilel_encoding,
ayoub_encoding,
arbi_encoding,
ali_encoding,
farah_encoding
]

known_faces_names = ["bilel","ayoub","arbi","ali","farah"]


def generate_id():
    return str(uuid.uuid4())
s=True
engine = pyttsx3.init()
def detect_faces(image: np.ndarray):
                # haarclassifiers work better in black and white
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                face_encodings = []
                
                name=""
                if s:
                        face_locations = face_recognition.face_locations(image)
                        face_encodings = face_recognition.face_encodings(image)
                        #face_names = []
                        for face_encoding in face_encodings:

                                matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
                                
                                face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
                                best_match_index = np.argmin(face_distance)
                                if matches[best_match_index]:
                                        name = known_faces_names[best_match_index]
                        
                                #face_names.append(name)
                                   

                return faces,name

def image_data_slot(image_data):
                
    faces,name = detect_faces(image_data)
    for (x, y, w, h) in faces:
            cv2.rectangle(image_data,(x,y),(x+w,y+h),(0,255,0),2)

    if name in known_faces_names:
                            
                            

                            font = cv2.FONT_HERSHEY_SIMPLEX
                            bottomLeftCornerOfText = (10,100)
                            fontScale              = 1.5
                            fontColor              = (0,255,0)
                            thickness              = 3
                            lineType               = 2
                            NameUser=name
                            # cv2.putText(image_data,'Welcome '+name, 
                            # bottomLeftCornerOfText, 
                            # font, 
                            # fontScale,
                            # fontColor,
                            # thickness,
                            # lineType) 
                            engine.say('Hello .'+name +' . How . are . you')
                            voices = engine.getProperty('voices')
                            engine.setProperty('voice', voices[1].id)
                            engine.runAndWait()
    # cv2.imshow('img',image_data)
# def detect_face(img):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     #print(faces)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = img[y:y+h, x:x+w]
        
#         #cv2.putText(img, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
#     #cv2.imshow('img',img)


while True:
    ret, img = cap.read()
    #img=test_image
   
    image_data_slot(img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#cap.release()
cv2.destroyAllWindows()