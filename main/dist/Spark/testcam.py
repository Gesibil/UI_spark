import cv2
import uuid
import face_recognition
import numpy as np
import pyttsx3
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

# Encoding faces
bilel_img = face_recognition.load_image_file("bilel.png")
bilel_encoding = face_recognition.face_encodings(bilel_img)[0]
bilel_img2 = face_recognition.load_image_file("bilel2.png")
bilel_encoding2 = face_recognition.face_encodings(bilel_img2)[0]

ayoub_img = face_recognition.load_image_file("ayoub.png")
ayoub_encoding = face_recognition.face_encodings(ayoub_img)[0]

firas_img = face_recognition.load_image_file("firas.png")
firas_encoding = face_recognition.face_encodings(firas_img)[0]
firas_img2 = face_recognition.load_image_file("firas2.png")
firas_encoding2 = face_recognition.face_encodings(firas_img2)[0]

wael_img = face_recognition.load_image_file("wael.png")
wael_encoding = face_recognition.face_encodings(firas_img)[0]
wael_img2 = face_recognition.load_image_file("wael2.png")
wael_encoding2 = face_recognition.face_encodings(firas_img2)[0]

arbi_img = face_recognition.load_image_file("arbi.png")
arbi_encoding = face_recognition.face_encodings(arbi_img)[0]
arbi_img2 = face_recognition.load_image_file("arbi2.png")
arbi_encoding2 = face_recognition.face_encodings(arbi_img2)[0]

ali_img = face_recognition.load_image_file("Ali.png")
ali_encoding = face_recognition.face_encodings(ali_img)[0]
ali_img2 = face_recognition.load_image_file("ali2.png")
ali_encoding2 = face_recognition.face_encodings(ali_img2)[0]

farah_img = face_recognition.load_image_file("farah.png")
farah_encoding = face_recognition.face_encodings(farah_img)[0]


ahdi_img = face_recognition.load_image_file("ahdi.png")
ahdi_encoding = face_recognition.face_encodings(ahdi_img)[0]


badii_img = face_recognition.load_image_file("badii.png")
badii_encoding = face_recognition.face_encodings(badii_img)[0]

taher_img = face_recognition.load_image_file("taher.png")
taher_encoding = face_recognition.face_encodings(taher_img)[0]
taher_img2 = face_recognition.load_image_file("taher2.png")
taher_encoding2 = face_recognition.face_encodings(taher_img2)[0]

rania_img = face_recognition.load_image_file("rania2.png")
rania_encoding = face_recognition.face_encodings(rania_img)[0]
rania_img2 = face_recognition.load_image_file("rania2.png")
rania_encoding2 = face_recognition.face_encodings(rania_img2)[0]

manel_img = face_recognition.load_image_file("manel.png")
manel_encoding = face_recognition.face_encodings(manel_img)[0]
manel_img2= face_recognition.load_image_file("manel2.png")
manel_encoding2 = face_recognition.face_encodings(manel_img2)[0]


known_face_encoding = [
    bilel_encoding,
    bilel_encoding2,
    ayoub_encoding,
    arbi_encoding,
    arbi_encoding2,
    ali_encoding,
    ali_encoding2,
    farah_encoding,
    ahdi_encoding,
    badii_encoding,
    taher_encoding,
    taher_encoding2,
    rania_encoding,
    rania_encoding2,
    manel_encoding,
    manel_encoding2,
    firas_encoding,
    firas_encoding2,
    wael_encoding,
    wael_encoding2

    
]

known_faces_names = [
    "bilel","bilel",
    "ayoub",
    "arbi","arbi",
    "ali","ali",
    "farah","aahdi","badii",
    "taher","taher",
    "rania", "rania",
    "manel","manel",
    "firas","firas",
    "wael","wael"]

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Dictionary to store face ID and last time said hello
face_dict = {}

def generate_id():
    return str(uuid.uuid4())

def detect_faces(image: np.ndarray):
    # haarclassifiers work better in black and white
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    face_encodings = []
    name = ""

    # Detect face using face_recognition library
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
        best_match_index = np.argmin(face_distance)
        if matches[best_match_index]:
            name = known_faces_names[best_match_index]

    return faces, name

def say_hello_to_face(name):
    # Check if it's time to say hello to this face again
    if name in face_dict:
        last_time_said_hello = face_dict[name]["last_time_said_hello"]
        if time.time() - last_time_said_hello < 10:
            return

    # Say hello and store the last time said hello
    engine.say('Hello ' + name + '. How are you .?')
    engine.runAndWait()
    face_dict[name] = {
        "id": generate_id(),
        "last_time_said_hello": time.time()
    }

while True:
    ret, img = cap.read()
    faces, name = detect_faces(img)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if name in known_faces_names:
        say_hello_to_face(name)

    # cv2.imshow('img', img)
    k = cv2.waitKey(30)
    if k == 27:
        break
cv2.destroyAllWindows()

