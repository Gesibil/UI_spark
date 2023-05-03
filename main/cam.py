import cv2
import uuid

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
#test_image = cv2.imread('image_zoomed.png')

face_dict = {}

def generate_id():
    return str(uuid.uuid4())


def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        #cv2.putText(img, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    cv2.imshow('img',img)


while True:
    ret, img = cap.read()
    #img=test_image
   
    detect_face(img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#cap.release()
cv2.destroyAllWindows()