# !/usr/bin/env python3

import sys


from os import path


from settings import*

import subprocess
import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon
from subprocess import call, Popen, PIPE, check_output
from PyQt5 import QtCore, QtGui, QtWidgets,QtChart
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
from PyQt5.QtChart import QChart, QLineSeries, QValueAxis

import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import face_recognition
# Import the required module for text 
# to speech conversion
import pyttsx3


#battery state 
battery_images = {
      
    0: "discharging_0.png",
    10: "discharging_10.png",
    20: "discharging_20.png",
    30: "discharging_30.png",
    40: "discharging_40.png",
    50: "discharging_50.png",
    60: "discharging_60.png",
    70: "discharging_70.png",
    80: "discharging_80.png",
    90: "discharging_90.png",
    100: "discharging_100.png"
}


xmlFile = et.parse('environment.xml')
# Find the root element from the file (in this case "environment")
root = xmlFile.getroot()
# Load the XML values from environment file


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

class Ui_MainWindow(QDialog):

    def startAnimation(self):
        self.movie.start()
  
    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()
    #emergency function 
    def EmergencyButtonstate(self):

        self.EmergencyButton.setDown(True)
        print('Shutting Down the Turtlebot...')
        QTimer.singleShot(5000, lambda: self.robotDownButton.setDown(False))
        # For localserver use this code:
        killRosNode = 'rosnode kill -a'
        killRosMaster = 'killall -9 rosmaster'
        killRosCore = 'killall -9 roscore'
        # Using Popen instead of Call because the first one don't block the process
        nodeKillProcess = subprocess.Popen(killRosNode, stdout=PIPE,
                                        stdin=PIPE, shell=True)
        masterKillProcess = subprocess.Popen(killRosMaster, stdout=PIPE,
                                            stdin=PIPE, shell=True)
        coreKillProcess = subprocess.Popen(killRosCore, stdout=PIPE,
                                        stdin=PIPE, shell=True)
        


    def update_battery(self):
        # Get the current battery percentage
        #output = subprocess.check_output(['acpi', '-b'])
        battery_percent = 0#int(re.findall(r'\d+%', output.decode())[0].strip('%'))

        # Map the battery percentage to the corresponding image file
        if battery_percent in battery_images:
            image_path = battery_images[battery_percent]
        else:
            image_path = self.battery_images[0]

        # Load the image and set it to the label
        pixmap = QtGui.QPixmap(image_path)
        self.batteryState.setPixmap(pixmap)
        return pixmap
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        self.title = "Spark"
        #MainWindow.setStyleSheet("background-image: url(/home/spark/TurtleUI-master/main/image_logo/eyes.gif);background-repeat: no-repeat;background-position: center;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        #self.centralwidget.setStyleSheet("background-image: url(/home/spark/TurtleUI-master/main/image_logo/eyes.gif);background-repeat: no-repeat;background-position: center;")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background: #000814")
        # Create a horizontal layout for the central widget
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

       
        # Add the logo label to the layout
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setPixmap(QtGui.QPixmap("logo&.png"))
        self.logoLabel.setMaximumSize(100, 100)
        self.logoLabel.setGeometry(QtCore.QRect(0, 0, 80, 80)) # Set the geometry of the logo label
        self.logoLabel.setScaledContents(True)
        
          # Add the logo label to the layout
        self.logoorange = QtWidgets.QLabel(self.centralwidget)
        self.logoorange.setPixmap(QtGui.QPixmap("orange.png"))
        self.logoorange.setMaximumSize(100, 100)
        self.logoorange.setGeometry(QtCore.QRect(640, 0, 80, 80)) # Set the geometry of the logo label
        self.logoorange.setScaledContents(True)
        
        #Create gif label and add it to the layout
        self.labelgif = QtWidgets.QLabel(self.centralwidget)
        self.labelgif.setGeometry(QtCore.QRect(0, 0, 720, 480))
        self.labelgif.setScaledContents(True)

        # Loading the GIF
        self.movie = QMovie("eyes-.gif")
        self.labelgif.setMovie(self.movie)
        self.startAnimation()
        self.horizontalLayout.addWidget(self.labelgif)

        # self.labelgif = QtWidgets.QLabel(self.centralwidget)
        # self.labelgif.setGeometry(QtCore.QRect(0, 0, 300, 480))
        # self.labelgif.setScaledContents(True)
        # self.labelgif1 = QtWidgets.QLabel(self.centralwidget)
        # self.labelgif1.setGeometry(QtCore.QRect(360, 0, 300, 480))
        # self.labelgif1.setScaledContents(True)
        # # Loading the GIF
        # self.movie = QMovie("ai-electricity.gif")
        # self.labelgif.setMovie(self.movie)
        # self.startAnimation()
        # self.horizontalLayout.addWidget(self.labelgif)
        # # Loading the GIF
        # self.movie = QMovie("ai-electricity.gif")
        # self.labelgif1.setMovie(self.movie)
        # self.startAnimation()
        # self.horizontalLayout.addWidget(self.labelgif1)

        #battery state
        self.batteryState = QtWidgets.QLabel(self.centralwidget)
        self.batteryState.setGeometry(QtCore.QRect(680, 450, 25, 20))
        pixmap = self.update_battery()
        transform = QtGui.QTransform().rotate(90)
        pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
        self.batteryState.setPixmap(pixmap)
        self.batteryState.setMaximumSize(120, 80)
        self.batteryState.setScaledContents(True)
        


        #button to switch screen
        icon = QtGui.QPixmap("login-.png")
        
        self.Screen2button = QPushButton(self.centralwidget)
        icon = icon.scaled(self.Screen2button.width(),self.Screen2button.height(),QtCore.Qt.KeepAspectRatio)
        self.Screen2button.setIcon(QtGui.QIcon(icon))
        self.Screen2button.setGeometry(QtCore.QRect(300, 0, 120, 120))
        self.Screen2button.clicked.connect(self.goScreen2)
        self.Screen2button.setToolTip('Authentificate')
        self.Screen2button.setStyleSheet("background: transparent; border: none;")
        

        self.batteryState.raise_()
        self.logoLabel.raise_()
        self.logoorange.raise_()
        self.Screen2button.raise_()
        # Set the central widget of the MainWindow
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def goScreen2(self):
        MainWindow.setCentralWidget(screenpage2)
        print("pressed")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spark"))


    # Define a class for recording video
class RecordVideo(QtCore.QObject):
    # Signal to emit the captured image data
    image_data = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, camera_port=0, parent=None):
        super().__init__(parent)
        # Initialize the camera by capturing the video from the specified camera port
        self.camera = cv2.VideoCapture(camera_port)
        self.timer = QtCore.QBasicTimer()

    def start_recording(self):
        # Start the timer to capture video frames
        self.timer.start(0, self)

    def stop_recording(self):
        # Stop the timer and release the camera resources
        self.timer.stop()
        self.camera.release()

    def timerEvent(self, event):
        # Check if the timer event is not from this class instance
        if event.timerId() != self.timer.timerId():
            return

        # Read a frame from the camera
        read, image = self.camera.read()
        if read:
            # Emit the captured image data using the defined signal
            self.image_data.emit(image)






class FaceDetectionWidget(QtWidgets.QWidget):


        def __init__(self,  parent=None):
                super().__init__(parent)
                self.classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                self.image = QtGui.QImage()
                self.NameUser='Admin'
                self.engine = pyttsx3.init()
                

        def detect_faces(self, image: np.ndarray):
                # haarclassifiers work better in black and white
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # Detect faces using the cascade classifier
                faces = self.classifier.detectMultiScale(gray, 1.3, 5)
                face_encodings = []
                
                name=""
                # Perform face recognition if face_encodings are available
                if s:
                        # Get face locations and encodings using face_recognition library
                        face_locations = face_recognition.face_locations(image)
                        face_encodings = face_recognition.face_encodings(image)
                        #face_names = []
                        for face_encoding in face_encodings:
                                # Perform face matching and retrieve the best match
                                matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
                                
                                face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
                                best_match_index = np.argmin(face_distance)
                                if matches[best_match_index]:
                                        name = known_faces_names[best_match_index]
                        
                                #face_names.append(name)
                                   

                return faces,name

        def image_data_slot(self, image_data):
                # Display user-specific information when a known face is recognized
            
                
               
                # Perform face detection on the incoming image data
                faces,name = self.detect_faces(image_data)
                 # Draw rectangles around detected faces
                for (x, y, w, h) in faces:
                        cv2.rectangle(image_data,(x,y),(x+w,y+h),(0,255,0),2)

                if name in known_faces_names:
                                        
                                        # Set up text properties

                                        font = cv2.FONT_HERSHEY_SIMPLEX
                                        bottomLeftCornerOfText = (10,100)
                                        fontScale              = 1.5
                                        fontColor              = (0,255,0)
                                        thickness              = 3
                                        lineType               = 2
                                        self.NameUser=name
                                        # Update the NameUser variable and speak a welcome message
                                        self.engine.say('Welcome '+name)
                                        voices = self.engine.getProperty('voices')
                                        self.engine.setProperty('voice', voices[0].id)
                                        self.engine.runAndWait()
                                         # Update the central widget of the main window to userpage
          
                                        MainWindow.setCentralWidget(userpage)
                # Convert the modified image to QImage for display        
                self.image = self.get_qimage(image_data)
                # Adjust the size of the widget based on the image size
                if self.image.size() != self.size():
                        self.setFixedSize(self.image.size())
                # Update the widget to trigger paintEvent
                self.update()

        def get_qimage(self, image: np.ndarray):
                # Convert the image data to QImage
                height, width, colors = image.shape
                bytesPerLine = 3 * width
                QImage = QtGui.QImage

                image = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)

                image = image.rgbSwapped()
                return image
        # Draw the image on the widget
        def paintEvent(self, event):
                painter = QtGui.QPainter(self)
                painter.drawImage(0, 0, self.image)
                self.image = QtGui.QImage()


s= True
class Screen3(QtWidgets.QWidget):
        def __init__(self, parent=None):
                super().__init__(parent)
                
                #fp = haarcascade_filepath
                self.face_detection_widget = FaceDetectionWidget()
                self.setupui(MainWindow)

        

        def setupui(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(720, 480)
            MainWindow.setStyleSheet("background-color: #000814;")
            self.title = "Spark"
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            
            
            # set video port
            self.record_video = RecordVideo(0)
            self.run_button = QtWidgets.QPushButton('Authentificate')
            self.run_button.setStyleSheet("color:#ffffff")
            
            # Connect the image data signal and slot together
            image_data_slot = self.face_detection_widget.image_data_slot
            
            self.record_video.image_data.connect(image_data_slot)
            # connect the run button to the start recording slot
            self.run_button.clicked.connect(self.record_video.start_recording)

            # Create and set the layout
            layout = QtWidgets.QVBoxLayout(self.centralwidget)
            layout.addWidget(self.face_detection_widget)
            layout.addWidget(self.run_button)
            

            


            #button to switch screen
            icon1 = QtGui.QPixmap("login.png")
            
            self.Screen3button1 = QPushButton(self.centralwidget)
            icon1 = icon1.scaled(self.Screen3button1.width(),self.Screen3button1.height(),QtCore.Qt.KeepAspectRatio)
            self.Screen3button1.setIcon(QtGui.QIcon(icon1))
            self.Screen3button1.setGeometry(QtCore.QRect(620, 0, 120, 120))
            self.Screen3button1.clicked.connect(self.goScreen1)
            self.Screen3button1.setToolTip('Authentificate')
            self.Screen3button1.setStyleSheet("background: transparent; border: none;")
            

            
            self.Screen3button1.raise_()
            layout.addWidget(self.Screen3button1)
            self.setLayout(layout)
            # Set the central widget of the MainWindow
            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Spark"))

        def goScreen1(self):
            MainWindow.setCentralWidget(Ui_MainWindow)
            print("pressed")

#Authentification screen

class Screen2(QtWidgets.QWidget):

        def __init__(self, parent=None):
                super().__init__(parent)
                
                self.setupui(MainWindow)

        

        def setupui(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(720, 480)
            MainWindow.setStyleSheet("background-color: #000814;")
          
            self.title = "Spark"
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")

            # Create a QVBoxLayout to hold the label and the button layout
            vbox = QtWidgets.QVBoxLayout(self.centralwidget)
            vbox.setSpacing(0)
            vbox.setContentsMargins(0, 0, 0, 0)
            
            # Create a QHBoxLayout
            hbox = QtWidgets.QHBoxLayout()
            hbox.setSpacing(0)
            hbox.setContentsMargins(0, 0, 0, 0)


            # Create a QLabel widget to display the image
            self.image_login = QtWidgets.QLabel(self.centralwidget)
            pixmap = QtGui.QPixmap('user.png')
            pixmap = pixmap.scaled(200, 100, QtCore.Qt.KeepAspectRatio)
            self.image_login.setPixmap(pixmap)
            self.image_login.setAlignment(QtCore.Qt.AlignCenter)

            # Add the image label widget to the vbox layout
            vbox.addWidget(self.image_login)

            # Add label widget to display text
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setText("Authentication Methods")
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
            vbox.addWidget(self.label)
            
            self.button1 = QtWidgets.QPushButton(self.centralwidget)
            self.button1.setGeometry(QtCore.QRect(0, 0,360, 410))
            icon1 = QtGui.QIcon('faceid.jpg')
            self.button1.setIcon(icon1)
            self.button1.setIconSize(QtCore.QSize(350, 410))
            self.button1.setStyleSheet("background: transparent; border: none;")
            self.button1.setToolTip('Authenticate by FACE ID')
            # Set the tooltip text color
            palette = QtGui.QPalette()
            palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor("#FFFFFF"))
            QtWidgets.QApplication.instance().setPalette(palette)

            
            self.button1.clicked.connect(self.goScreen3)
            hbox.addWidget(self.button1)

            self.button2 = QtWidgets.QPushButton(self.centralwidget)
            self.button2.setGeometry(QtCore.QRect(360, 0,360, 430))
            icon2 = QtGui.QIcon('aut.png')
            self.button2.setIcon(icon2)
            self.button2.setIconSize(QtCore.QSize(350, 430))
            self.button2.setStyleSheet("background: transparent; border: none;")
            self.button2.setToolTip('Authentificate by Key ')
            # Set the tooltip text color
            palette = QtGui.QPalette()
            palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor("#FFFFFF"))
            QtWidgets.QApplication.instance().setPalette(palette)
            hbox.addWidget(self.button2)
            self.button2.clicked.connect(self.gologin)
            vbox.addLayout(hbox)
            self.centralwidget.setLayout(vbox)
            

            self.setLayout(vbox)
            # Set the central widget of the MainWindow
            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Spark"))

        def goScreen3(self):
            MainWindow.setCentralWidget(screenpage3)
            print("Faceid page")

        def gologin(self):
            MainWindow.setCentralWidget(loginpage)
            print("loginpage")

#user name authentification

class login(QtWidgets.QWidget):
    def __init__(self, parent=None):
                super().__init__(parent)
                
                self.setupUi(MainWindow)

    
    def setupUi(self, MainWindow):            
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setStyleSheet("background-color: #000814;")

        self.bgwidget = QtWidgets.QWidget(MainWindow)
        self.bgwidget.setObjectName("bgwidget")
        vbox = QtWidgets.QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 20, 0, 0)
        self.image_login = QtWidgets.QLabel(self.bgwidget)
        pixmap = QtGui.QPixmap('user.png')
        pixmap = pixmap.scaled(200, 100, QtCore.Qt.KeepAspectRatio)
        self.image_login.setPixmap(pixmap)
        self.image_login.setAlignment(QtCore.Qt.AlignCenter)

        # Add the image label widget to the vbox layout
        vbox.addWidget(self.image_login)
        vbox.addStretch(1)
        # Add label widget to display login
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setText("Login")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        self.label.setObjectName("label")
        
        vbox.addWidget(self.label)
        vbox.addStretch(1)
        # Add label widget to display login
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setText("User Name")
        #self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_2.setGeometry(QtCore.QRect(300, 300, 100, 10))
        self.label_2.setStyleSheet("color: white; font-size: 20px;")

        self.label_2.setObjectName("label_2")
        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label_2)
        hbox.addStretch(1)
        
               
        self.emailfield = QtWidgets.QLineEdit(self.bgwidget)
        #self.emailfield.setGeometry(QtCore.QRect(0,80, 0, 10))
        #self.emailfield.setAlignment(QtCore.Qt.AlignCenter)
        self.emailfield.setStyleSheet("background-color:#0095BE;\n"
        "font: 12pt \"MS Shell Dlg 2\";")
        self.emailfield.setObjectName("emailfield")
        
        
        hbox.addWidget(self.emailfield)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setText("Password")
        #self.label_2.setAlignment(QtCore.Qt.AlignLeft)
        #self.label_3.setGeometry(QtCore.QRect(0, 300, 100, 10))
        self.label_3.setStyleSheet("color: white; font-size: 20px;")

        self.label_3.setObjectName("label_2")
        hbox2 = QtWidgets.QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.label_3)
        hbox2.addStretch(1)
        self.passwordfield = QtWidgets.QLineEdit(self.bgwidget)
        self.passwordfield.setGeometry(QtCore.QRect(0, 140, 341, 51))
        self.passwordfield.setStyleSheet("background-color:#0095BE;\n"
        "font: 12pt \"MS Shell Dlg 2\";")
        self.passwordfield.setObjectName("passwordfield")
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        
        hbox2.addWidget(self.passwordfield)
        hbox2.addStretch(1)

        vbox.addLayout(hbox2)
        
        vbox.addStretch(1)

        self.login = QtWidgets.QPushButton(self.bgwidget)
        self.login.setGeometry(QtCore.QRect(0, 0, 300, 80))
        self.login.setStyleSheet("border-radius:5px;\n"
                                "background-color: #0095BE;\n"
                                "font: 12pt \"MS Shell Dlg 2\";")
        self.login.setObjectName("login")
        self.login.setText("Login")
        self.login.clicked.connect(self.goUserpage)
       

        hbox3 = QtWidgets.QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.login)
        hbox3.addStretch(1)

        vbox.addLayout(hbox3)
        vbox.addStretch(1)
        
        
        
        self.setLayout(vbox)
        MainWindow.setCentralWidget(self.bgwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spark"))

    def userData(self):
          email=self.emailfield.text()
          pwd=self.passwordfield.text()
          return email,pwd
    def goUserpage(self):
        u,p=self.userData()
        print(u,p)
        if (u=="admin" and p=="admin"):
              MainWindow.setCentralWidget(userpage)

        else:
        # show error message
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Invalid username or password")
            error_dialog.setWindowTitle("Error")
            error_dialog.setStyleSheet("background-color: #000814; color: white;")
            error_dialog.exec_()
          
          


#admin interface 
class User(QtWidgets.QWidget):
    def __init__(self,username='admin',password='admin',parent=None):
                super().__init__(parent)
                self.username = username
                self.password = password
                self.bgwidget = QtWidgets.QWidget(MainWindow)
                self.vbox = QtWidgets.QVBoxLayout(self.bgwidget)
                self.vbox.setSpacing(0)
                self.vbox.setContentsMargins(0, 0, 0, 0)

                self.hbox = QtWidgets.QVBoxLayout(self.bgwidget)
                self.hbox.setSpacing(0)
                self.hbox.setContentsMargins(0, 0, 0, 0)
                self.face=FaceDetectionWidget()

                self.grid_layout = QtWidgets.QGridLayout(self.bgwidget)
                self.grid_layout.setSpacing(0)
                self.grid_layout.setContentsMargins(0, 0, 0, 0) 
                
                self.setupUi(MainWindow)
                self.record_video = RecordVideo(0)
                self.record_video.stop_recording()
                

    
        
    def setupUi(self, MainWindow):            
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setStyleSheet("background-color: #000814;")

        
        self.bgwidget.setObjectName("bgwidget")
        # vbox = QtWidgets.QVBoxLayout(self.bgwidget)
        # vbox.setSpacing(0)
        # vbox.setContentsMargins(0, 0, 0, 0)
         # Add label widget to display text
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setText("Welcome "+self.face.NameUser)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        self.hbox.addWidget(self.label)  

        #self.setLayout(self.vbox)
        MainWindow.setCentralWidget(self.bgwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spark"))  


    def gobattery(self):
          MainWindow.setCentralWidget(battery_chart) 


     




class AdminUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.admin = True  
        self.vbox = QtWidgets.QVBoxLayout(self.bgwidget)
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(0, 0, 0, 0) 

        self.hbox = QtWidgets.QVBoxLayout(self.bgwidget)
        self.hbox.setSpacing(0)
        self.hbox.setContentsMargins(0, 0, 0, 0) 

        self.grid_layout = QtWidgets.QGridLayout(self.bgwidget)
        self.grid_layout.setSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0) 
        

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        
        self.icon1 = QtWidgets.QPushButton(self.bgwidget)
        self.icon2 = QtWidgets.QPushButton(self.bgwidget)
        self.icon3 = QtWidgets.QPushButton(self.bgwidget)
        self.icon4 = QtWidgets.QPushButton(self.bgwidget)

        # Set icons for each button
        icon1_path = 'setting.png'
        self.icon1.setIcon(QtGui.QIcon(icon1_path))
        self.icon1.setIconSize(QtCore.QSize(50,50))
        self.icon1_label = QtWidgets.QLabel("Settings", self.bgwidget)
        self.grid_layout.addWidget(self.icon1_label, 1, 0)
        self.icon1.clicked.connect(settings)

        icon2_path = 'charging.png'
        self.icon2.setIcon(QtGui.QIcon(icon2_path))
        self.icon2.setIconSize(QtCore.QSize(50,50))
        self.icon2.clicked.connect(lambda: self.show_battery_chart())

        icon3_path = 'placeholder.png'
        self.icon3.setIcon(QtGui.QIcon(icon3_path))
        self.icon3.setIconSize(QtCore.QSize(50,50))
        self.icon3.clicked.connect(lambda: self.shoose_maps())

        icon4_path = 'conference_.png'
        self.icon4.setIcon(QtGui.QIcon(icon4_path))
        self.icon4.setIconSize(QtCore.QSize(50,50))
        self.admin_image=QtWidgets.QLabel(self.bgwidget)
        pixmap = QtGui.QPixmap('adminicon.png')
        pixmap = pixmap.scaled(200, 100, QtCore.Qt.KeepAspectRatio)
        self.admin_image.setPixmap(pixmap)
        self.admin_image.setAlignment(QtCore.Qt.AlignCenter)
        self.hbox.addWidget(self.admin_image)

        # # Add buttons to the layout
        # self.grid_layout.addWidget(self.icon1,0,0)
        # self.grid_layout.addWidget(self.icon2,0,1)
        # self.grid_layout.addWidget(self.icon3,1,0)
        # self.grid_layout.addWidget(self.icon4,1,1)
        # # Add text labels for each icon
        # self.text1 = QtWidgets.QLabel("Settings", self.bgwidget)
        # self.text2 = QtWidgets.QLabel("battery status", self.bgwidget)
        # self.text3 = QtWidgets.QLabel("maps and position", self.bgwidget)
        # self.text4 = QtWidgets.QLabel("visio-Conference", self.bgwidget)
        
            # Create labels for each button
        self.label1 = QtWidgets.QLabel('Settings', self.bgwidget)
        self.label2 = QtWidgets.QLabel('Battery status', self.bgwidget)
        self.label3 = QtWidgets.QLabel('Maps and position', self.bgwidget)
        self.label4 = QtWidgets.QLabel('Visio-Conference', self.bgwidget)

        # Set the font size and color for the labels
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtGui.QColor(255, 255, 255))
        self.label1.setFont(font)
        self.label1.setPalette(palette)
        self.label2.setFont(font)
        self.label2.setPalette(palette)
        self.label3.setFont(font)
        self.label3.setPalette(palette)
        self.label4.setFont(font)
        self.label4.setPalette(palette)

        # Add buttons and labels to the grid layout
        self.grid_layout.addWidget(self.label1, 0, 0)
        self.grid_layout.addWidget(self.icon1, 1, 0)
        self.grid_layout.addWidget(self.label2, 0, 1)
        self.grid_layout.addWidget(self.icon2, 1, 1)
        self.grid_layout.addWidget(self.label3, 2, 0)
        self.grid_layout.addWidget(self.icon3, 3, 0)
        self.grid_layout.addWidget(self.label4, 2, 1)
        self.grid_layout.addWidget(self.icon4, 3, 1)

        # Add text labels to the layout
        # self.grid_layout.addWidget(self.text1, 1, 0, QtCore.Qt.AlignHCenter)
        # self.grid_layout.addWidget(self.text2, 1, 1, QtCore.Qt.AlignHCenter)
        # self.grid_layout.addWidget(self.text3, 2, 0, QtCore.Qt.AlignHCenter)
        # self.grid_layout.addWidget(self.text4, 2, 1, QtCore.Qt.AlignHCenter)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.grid_layout)
        
        

        self.setLayout(self.vbox)
    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spark"))
        #self.icon1.setText(_translate("MainWindow", "Settings"))

    def show_battery_chart(self):
        battery_chart = BatteryChart(self)
        battery_chart.exec_()

    def shoose_maps(self):
        maps = Maps(self)
        maps.exec_()

    def showRVIZ(self):
        host_name='export ROS_HOSTNAME=localhost'
        rosmuster_URI='export ROS_MASTER_URI=http://localhost:11311'
        rvizCommand = 'rviz'
        hostnameProcess = subprocess.Popen(host_name, stdout=PIPE,
                                       stdin=PIPE, shell=True)
        RosMasterProcess = subprocess.Popen(rosmuster_URI, stdout=PIPE,
                                       stdin=PIPE, shell=True)
        
        rvizProcess = subprocess.Popen(rvizCommand, stdout=PIPE,
                                       stdin=PIPE, shell=True)
        
    
            



class SimpleUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.admin = False
        self.vbox = QtWidgets.QVBoxLayout(self.bgwidget)
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(0, 0, 0, 0)




class Maps(QDialog):
    def __init__(self, parent=None):
        super().__init__(None)
        self.setupUi()

        
    def setupUi(self):
        self.maps = QtWidgets.QWidget()
        self.setWindowTitle("Choose map")
        self.setStyleSheet("background: #0a182b;")
        self.setMinimumSize(QtCore.QSize(600, 400))
        self.FirstFloor = QtWidgets.QPushButton(self)
        self.FirstFloor.setGeometry(QtCore.QRect(180, 50, 50, 50))  # Set the position and size of the button
        iconfloor_path = 'blueprint.png'
        self.FirstFloor.setIcon(QtGui.QIcon(iconfloor_path))
        self.FirstFloor.setIconSize(QtCore.QSize(50, 50))
        floor1="3rdfloor.yaml"
        self.FirstFloor.clicked.connect(lambda: self.modify_launch_file(floor1))

        self.SecondFloor = QtWidgets.QPushButton(self)
        self.SecondFloor.setGeometry(QtCore.QRect(180, 230, 50, 50))  # Set the position and size of the button
        iconfloor_path = 'blueprint.png'
        self.SecondFloor.setIcon(QtGui.QIcon(iconfloor_path))
        self.SecondFloor.setIconSize(QtCore.QSize(50, 50))
        floor2="Secondfloor.yaml"
        self.SecondFloor.clicked.connect(lambda: self.modify_launch_file(floor2))


        self.label1 = QtWidgets.QLabel(' Third Floor (Default map)', self)
        self.label1.setGeometry(QtCore.QRect(300, 110, 200, 50))

        self.label2 = QtWidgets.QLabel(' 2nd Floor ', self)
        self.label2.setGeometry(QtCore.QRect(320, 300, 200, 50))
         # Set the font size and color for the labels
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtGui.QColor(255, 255, 255))
        self.label1.setFont(font)
        self.label1.setPalette(palette)
        self.label2.setFont(font)
        self.label2.setPalette(palette)


        # Create a label to display the image
        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setGeometry(QtCore.QRect(300, 30, 200, 80))
        self.image_label.setPixmap(QtGui.QPixmap("3rdfloor.PNG"))
        self.image_label.setScaledContents(True)

        self.image_label2 = QtWidgets.QLabel(self)
        self.image_label2.setGeometry(QtCore.QRect(300, 220, 200, 80))
        self.image_label2.setPixmap(QtGui.QPixmap("2ndfloor.jpg"))
        self.image_label2.setScaledContents(True)

        self.label1.raise_()
        self.label2.raise_()
        self.image_label.raise_()
        self.image_label2.raise_()
        
        self.retranslateUi(MainWindow)
        #self.maps.setCentralWidget(self.maps)
    def modify_launch_file(self,floor):
    # Open the launch file
        launch_file_path = "test.launch"
        with open(launch_file_path, "r") as f:
            launch_file_contents = f.read()
        
        oldpath = '<arg name="map_file" default="$(find navigation_data_pub)/maps/'+floor+'"/>'
        newpath = '<arg name="map_file" default="$(find navigation_data_pub)/maps/'+floor+'"/>'
        
        # Modify the launch file
        modified_launch_file_contents = launch_file_contents.replace(oldpath, newpath)

        # Save the modified launch file
        with open(launch_file_path, "w") as f:
            f.write(modified_launch_file_contents)
        print("launch file modified")
    

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label1.setText(_translate("MainWindow", "Third Floor (Default map)"))
        self.label2.setText(_translate("MainWindow", "2nd Floor"))
        


      

class BatteryChart(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        #QDialog.__init__(parent)
        self.setMinimumSize(QtCore.QSize(600, 400))
        self.setStyleSheet("background: #0a182b;")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setObjectName("verticalLayout")
         # Create the chart
        self.chart = QtChart.QChart()
        self.chart.setTitle("Battery Status")
        self.chart.setTitleBrush(QtGui.QBrush(QtGui.QColor("#ffffff")))
        self.chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        brush = QtGui.QBrush(QtGui.QColor(0, 8, 20))
        self.chart.setBackgroundBrush(brush)

        
        # Create the series and add it to the chart
        self.series = QtChart.QLineSeries()
        self.series.setName("Battery")
        self.chart.addSeries(self.series)


        
         # Create the axis and add them to the chart
        self.axis_x = QtChart.QDateTimeAxis()
        self.axis_x.setRange(QtCore.QDateTime.currentDateTime().addSecs(-8*60*60), QtCore.QDateTime.currentDateTime())
        time_format = "<font color='#ffffff'>hh</font>"
        self.axis_x.setFormat(time_format)
        self.axis_x.setTitleText("Time(h)")
        self.axis_x.setTitleBrush(QtGui.QBrush(QtGui.QColor("#ffffff")))
        self.chart.addAxis(self.axis_x, QtCore.Qt.AlignBottom)
        grid_color = QtGui.QColor("white")
        self.axis_x.setGridLineColor(grid_color)
        self.series.attachAxis(self.axis_x)
    
        
        self.axis_y = QtChart.QValueAxis()
        self.axis_y.setRange(0, 100)
        label_format = "<font color='#ffffff'>%d</font>"
        self.axis_y.setLabelFormat(label_format)
        #self.axis_y.setLabelFormat("%d%%")
        self.axis_y.setTitleText("Percentage")
        self.axis_y.setTitleBrush(QtGui.QBrush(QtGui.QColor("#ffffff")))
        self.chart.addAxis(self.axis_y, QtCore.Qt.AlignLeft)
        grid_color = QtGui.QColor("white")
        self.axis_y.setGridLineColor(grid_color)
       
        self.series.attachAxis(self.axis_y)
       
        
        # Create the chart view and set the chart as its model
        self.chart_view = QtChart.QChartView(self.chart)
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        
        
        self.layout.addWidget(self.chart_view)
        
       
        #self.setupUi(MainWindow)
        # Update the chart with some data
         # Update the chart with some data
        self.update_chart([(99, QtCore.QDateTime.currentDateTime().addSecs(-6*60*60)),
                           (80, QtCore.QDateTime.currentDateTime().addSecs(-4*60*60)),
                           (60, QtCore.QDateTime.currentDateTime().addSecs(-2*60*60)),
                           (40, QtCore.QDateTime.currentDateTime().addSecs(-1*60*60)),
                           (20, QtCore.QDateTime.currentDateTime().addSecs(-30*60)),
                           (5, QtCore.QDateTime.currentDateTime().addSecs(-10*60))])

        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spark"))
        
    def update_chart(self, data):
        # Add data points to the series
        for point in data:
            self.series.append(point[1].toMSecsSinceEpoch(), point[0])
        
        # Set the axis labels visible
        self.axis_x.setLabelsVisible(True)
        self.axis_y.setLabelsVisible(True)

    def returnscreen(self):
        MainWindow.setCentralWidget(userpage)
        print("pressed")

if __name__ == "__main__":
    # rospy.init_node('turtleui')
    # print('Running...')
    script_dir = path.dirname(path.realpath(__file__))
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    haar_cascade_filepath=path.join(script_dir, 'haarcascade_frontalface_default.xml')
    haar_cascade_filepath = path.abspath(haar_cascade_filepath)
    screenpage3=Screen3()
    screenpage2=Screen2()
    loginpage=login()
    battery_chart=BatteryChart()
    
    usr,pwd=loginpage.userData()
    userpage=AdminUser(usr,pwd)
    main = Ui_MainWindow()
    main.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
