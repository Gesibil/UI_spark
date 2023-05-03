import os
import sys
import subprocess
from subprocess import call, Popen, PIPE, check_output
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QTimer
try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

# Get the actual Script $PATH
scriptPath = str(os.getcwd())
print (scriptPath)
# Reads the XML File
xmlFile = et.parse('/home/ubuntu/TurtleUI-master/main/environment.xml')
# Find the root element from the file (in this case "environment")
root = xmlFile.getroot()
# Load the XML values from environment file
myIP = root.findtext('MY_IP')
rosNamespace = root.findtext('ROS_NAMESPACE')

# Values to Export into "~/.bashrc"
exportIP = str('ROS_IP='+myIP)
exportMasterIP = str('MASTER_IP='+myIP)
exportMasterIPURI = str('export ROS_MASTER_URI=http://$MASTER_IP:11311/')
exportRosIP = str('export ROS_IP=$MY_IP')
exportHostname = str('export ROS_HOSTNAME_IP=$MY_IP')
exportNamespace = str('export ROS_NAMESPACE='+rosNamespace)
subprocess.call('export ROS_MASTER_URI=http://localhost:11311', shell=True)

class settings(QDialog):
    def __init__(self, parent=None):
        # super(envConfig, self).__init__(parent)
        QDialog.__init__(self)
        envConfigDialog = QWidget(self)
        envConfigDialog.setObjectName("envConfigDialog")
        envConfigDialog.setWindowTitle("Settings")
        self.resize(340, 425)
        self.setMinimumSize(QtCore.QSize(340, 410))
        self.setStyleSheet("background: #000814;")
        self.tabbedConfig = QtWidgets.QTabWidget(envConfigDialog)
        self.tabbedConfig.setGeometry(QtCore.QRect(5, 10, 333, 411))
        self.tabbedConfig.setMinimumSize(QtCore.QSize(0, 0))
        self.tabbedConfig.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabbedConfig.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabbedConfig.setStyleSheet("background: #0a182b;\n"
                                        "color: rgb(199, 199, 199)")
        self.tabbedConfig.setObjectName("tabbedConfig")
        self.connectionConfig = QtWidgets.QWidget()
        self.connectionConfig.setObjectName("connectionConfig")
        self.envConfigTab = QtWidgets.QGroupBox(self.connectionConfig)
        self.envConfigTab.setGeometry(QtCore.QRect(5, 9, 321, 181))
        self.envConfigTab.setMinimumSize(QtCore.QSize(320, 140))
        self.envConfigTab.setStyleSheet("color: rgb(14, 172, 186);")
        self.envConfigTab.setObjectName("envConfigTab")
        self.myIP = QtWidgets.QLineEdit(self.envConfigTab)
        self.myIP.setGeometry(QtCore.QRect(90, 30, 231, 23))
        self.myIP.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                "color: rgb(199, 199, 199);")
        self.myIP.setDragEnabled(False)
        self.myIP.setObjectName("myIP")
        self.masterIP = QtWidgets.QLineEdit(self.envConfigTab)
        self.masterIP.setGeometry(QtCore.QRect(90, 60, 231, 23))
        self.masterIP.setStyleSheet("color: rgb(199, 199, 199);\n"
                                    "background: rgba(29, 222, 216, 0.1);")
        self.masterIP.setObjectName("masterIP")
        self.hostname = QtWidgets.QLineEdit(self.envConfigTab)
        self.hostname.setGeometry(QtCore.QRect(90, 118, 231, 23))
        self.hostname.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                    "color: rgb(199, 199, 199);")
        self.hostname.setObjectName("hostname")
        self.nameSpace = QtWidgets.QLineEdit(self.envConfigTab)
        self.nameSpace.setGeometry(QtCore.QRect(90, 148, 231, 23))
        self.nameSpace.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                     "color: rgb(199, 199, 199);")
        self.nameSpace.setObjectName("nameSpace")
        self.rosMyIPLabel = QtWidgets.QLabel(self.envConfigTab)
        self.rosMyIPLabel.setGeometry(QtCore.QRect(5, 32, 71, 16))
        self.rosMyIPLabel.setStyleSheet("color: rgb(199, 199, 199);")
        self.rosMyIPLabel.setObjectName("rosMyIPLabel")
        self.rosMasterIPLabel = QtWidgets.QLabel(self.envConfigTab)
        self.rosMasterIPLabel.setGeometry(QtCore.QRect(5, 62, 71, 16))
        self.rosMasterIPLabel.setStyleSheet("color: rgb(199, 199, 199);")
        self.rosMasterIPLabel.setObjectName("rosMasterIPLabel")
        self.rosHostnameLabel = QtWidgets.QLabel(self.envConfigTab)
        self.rosHostnameLabel.setGeometry(QtCore.QRect(5, 120, 71, 16))
        self.rosHostnameLabel.setStyleSheet("color: rgb(199, 199, 199);")
        self.rosHostnameLabel.setObjectName("rosHostnameLabel")
        self.rosNamespaceLabel = QtWidgets.QLabel(self.envConfigTab)
        self.rosNamespaceLabel.setGeometry(QtCore.QRect(5, 150, 81, 16))
        self.rosNamespaceLabel.setStyleSheet("color: rgb(199, 199, 199);")
        self.rosNamespaceLabel.setObjectName("rosNamespaceLabel")
        self.rosMasterIURILabel = QtWidgets.QLabel(self.envConfigTab)
        self.rosMasterIURILabel.setGeometry(QtCore.QRect(5, 90, 81, 16))
        self.rosMasterIURILabel.setStyleSheet("color: rgb(199, 199, 199);")
        self.rosMasterIURILabel.setObjectName("rosMasterIURILabel")
        self.masterURI = QtWidgets.QLineEdit(self.envConfigTab)
        self.masterURI.setGeometry(QtCore.QRect(90, 88, 231, 23))
        self.masterURI.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                     "color: rgb(199, 199, 199);")
        self.masterURI.setObjectName("masterURI")
        self.groupBox_2 = QtWidgets.QGroupBox(self.connectionConfig)
        self.groupBox_2.setGeometry(QtCore.QRect(5, 200, 320, 151))
        self.groupBox_2.setStyleSheet("color: rgb(14, 172, 186);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.shutdownButton = QtWidgets.QPushButton(self.groupBox_2)
        pixmap = QtGui.QPixmap('/home/ubuntu/TurtleUI-master/main/image_logo/shut-down.png')
        pixmap = pixmap.scaled(100, 50, QtCore.Qt.KeepAspectRatio)
        self.shutdownButton.setIcon(QtGui.QIcon(pixmap))
        self.shutdownButton.setIconSize(QtCore.QSize(100, 50))
        self.shutdownButton.setGeometry(QtCore.QRect(0, 20, 100, 50))
        self.shutdownButton.setStyleSheet("background: transparent; border: none;")
        self.shutdownButton.clicked.connect(self.shutdownButtonstate)
        self.shutdownButton.setToolTip('Shut-down the ROS ')
        # Set the tooltip text color
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor("#FFFFFF"))
        QtWidgets.QApplication.instance().setPalette(palette)

        self.restartButton = QtWidgets.QPushButton(self.groupBox_2)
        pixmap = QtGui.QPixmap('/home/ubuntu/TurtleUI-master/main/image_logo/loop.png')
        pixmap = pixmap.scaled(100, 50, QtCore.Qt.KeepAspectRatio)
        self.restartButton.setIcon(QtGui.QIcon(pixmap))
        self.restartButton.setIconSize(QtCore.QSize(100, 50))
        self.restartButton.setGeometry(QtCore.QRect(70, 20, 100, 50))
        self.restartButton.setStyleSheet("background: transparent; border: none;")
        self.restartButton.setToolTip('Restart the ROS ')
        self.restartButton.clicked.connect(self.restartButton_procc)

        # self.shutDown = QtWidgets.QPushButton(self.groupBox_2)
        # self.shutDown.setGeometry(QtCore.QRect(360, 0,360, 430))
        # icon2 = QtGui.QIcon('/home/ubuntu/TurtleUI-master/main/image_logo/shut-down.png')
        # self.shutDown.setIcon(icon2)
        # self.shutDown.setIconSize(QtCore.QSize(100, 100))
        # self.shutDown.setStyleSheet("background: transparent; border: none;")
        # self.shutDown.setToolTip('Authentificate by Key ')
        # # Set the tooltip text color
        # palette = QtGui.QPalette()
        # palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor("#FFFFFF"))
        # QtWidgets.QApplication.instance().setPalette(palette)

        # self.user = QtWidgets.QLineEdit(self.groupBox_2)
        # self.user.setGeometry(QtCore.QRect(110, 58, 210, 23))
        # self.user.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
        #                         "color: rgb(199, 199, 199);")
        # self.user.setObjectName("user")
        # self.password = QtWidgets.QLineEdit(self.groupBox_2)
        # self.password.setGeometry(QtCore.QRect(110, 88, 210, 23))
        # self.password.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
        #                             "color: rgb(199, 199, 199);")
        # self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.password.setObjectName("password")
        # self.portLabel = QtWidgets.QLabel(self.groupBox_2)
        # self.portLabel.setGeometry(QtCore.QRect(5, 120, 81, 16))
        # self.portLabel.setStyleSheet("color: rgb(199, 199, 199);")
        # self.portLabel.setObjectName("portLabel")
        # self.port = QtWidgets.QLineEdit(self.groupBox_2)
        # self.port.setGeometry(QtCore.QRect(110, 118, 210, 23))
        # self.port.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
        #                         "color: rgb(199, 199, 199);")
        # self.port.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        # self.port.setObjectName("port")
        # self.userLabel = QtWidgets.QLabel(self.groupBox_2)
        # self.userLabel.setGeometry(QtCore.QRect(5, 60, 71, 16))
        # self.userLabel.setStyleSheet("color: rgb(199, 199, 199);")
        # self.userLabel.setObjectName("userLabel")
        # self.turtlebotIP = QtWidgets.QLineEdit(self.groupBox_2)
        # self.turtlebotIP.setGeometry(QtCore.QRect(110, 28, 210, 23))
        # self.turtlebotIP.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
        #                                "color: rgb(199, 199, 199);")
        # self.turtlebotIP.setObjectName("turtlebotIP")
        # self.passwordLabel = QtWidgets.QLabel(self.groupBox_2)
        # self.passwordLabel.setGeometry(QtCore.QRect(5, 90, 81, 16))
        # self.passwordLabel.setStyleSheet("color: rgb(199, 199, 199);")
        # self.passwordLabel.setObjectName("passwordLabel")
        # self.turtlebotIPLabel = QtWidgets.QLabel(self.groupBox_2)
        # self.turtlebotIPLabel.setGeometry(QtCore.QRect(5, 30, 91, 16))
        # self.turtlebotIPLabel.setStyleSheet("color: rgb(199, 199, 199);")
        # self.turtlebotIPLabel.setObjectName("turtlebotIPLabel")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.connectionConfig)
        self.buttonBox.setGeometry(QtCore.QRect(120, 350, 171, 32))
        self.buttonBox.setStyleSheet("color: rgb(199, 199, 199);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.defaultButton = QtWidgets.QPushButton(self.connectionConfig)
        self.defaultButton.setGeometry(QtCore.QRect(40, 355, 80, 23))
        self.defaultButton.setStyleSheet("color: rgb(199, 199, 199);")
        self.defaultButton.setObjectName("defaultButton")
        self.tabbedConfig.addTab(self.connectionConfig, "")
        self.othersTab = QtWidgets.QWidget()
        self.othersTab.setObjectName("othersTab")
        self.description_label = QtWidgets.QLabel(self.othersTab)
        self.description_label.setGeometry(QtCore.QRect(0, 20, 300, 410))
        self.description_label.setAlignment(QtCore.Qt.AlignLeft)
        self.description_label.setWordWrap(True)
        self.description_label.setStyleSheet("color: white; font-size: 12pt;")
        self.description_label.setText("Spark , developed by the Innovation Lab of Sofrecom Tunisia, is an exciting project undertaken by Ayoub Ayari and Bilel Hammemi as part of their end-of-studies internship. This robot has been designed to provide a high-quality remote communication experience, enabling users to interact with others in real-time from remote locations. The user interface we are developing will provide a clear and concise view of Spark's status, allowing for easy monitoring of its various functionalities and ensuring seamless and reliable communication for users.")
        #self.rosSource = QtWidgets.QLineEdit(self.othersTab)
        # self.rosSource.setGeometry(QtCore.QRect(100, 50, 221, 23))
        # self.rosSource.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
        #                              "color: rgb(199, 199, 199);")
        # self.rosSource.setObjectName("rosSource")
        # self.perspectiveLabel = QtWidgets.QLabel(self.othersTab)
        # self.perspectiveLabel.setGeometry(QtCore.QRect(5, 22, 81, 16))
        # self.perspectiveLabel.setStyleSheet("color: rgb(199, 199, 199);")
        # self.perspectiveLabel.setObjectName("perspectiveLabel")
        # self.perspective = QtWidgets.QLineEdit(self.othersTab)
        # self.perspective.setGeometry(QtCore.QRect(100, 20, 221, 23))
        # self.perspective.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
        #                                "color: rgb(199, 199, 199);")
        # self.perspective.setObjectName("perspective")
        # self.rosETCDirectory = QtWidgets.QLineEdit(self.othersTab)
        # self.rosETCDirectory.setGeometry(QtCore.QRect(100, 80, 221, 23))
        # self.rosETCDirectory.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
        #                                    "color: rgb(199, 199, 199);")
        # self.rosETCDirectory.setObjectName("rosETCDirectory")
        # self.rosSourceLabel = QtWidgets.QLabel(self.othersTab)
        # self.rosSourceLabel.setGeometry(QtCore.QRect(5, 52, 91, 16))
        # self.rosSourceLabel.setStyleSheet("color: rgb(199, 199, 199);")
        # self.rosSourceLabel.setObjectName("rosSourceLabel")
        # self.rosETCDirectoryLabel = QtWidgets.QLabel(self.othersTab)
        # self.rosETCDirectoryLabel.setGeometry(QtCore.QRect(5, 82, 71, 16))
        # self.rosETCDirectoryLabel.setStyleSheet("color: rgb(199, 199, 199);")
        # self.rosETCDirectoryLabel.setObjectName("rosETCDirectoryLabel")
        # self.rosRoot = QtWidgets.QLineEdit(self.othersTab)
        # self.rosRoot.setGeometry(QtCore.QRect(100, 110, 221, 23))
        # self.rosRoot.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
        #                            "color: rgb(199, 199, 199);")
        # self.rosRoot.setObjectName("rosRoot")
        # self.rosRootLabel = QtWidgets.QLabel(self.othersTab)
        # self.rosRootLabel.setGeometry(QtCore.QRect(5, 112, 81, 16))
        # self.rosRootLabel.setStyleSheet("color: rgb(199, 199, 199);")
        # self.rosRootLabel.setObjectName("rosRootLabel")
        # DEFAULT
        self.defaultButtonTab2 = QtWidgets.QPushButton(self.othersTab)
        self.defaultButtonTab2.setGeometry(QtCore.QRect(40, 355, 80, 23))
        self.defaultButtonTab2.setStyleSheet("color: rgb(199, 199, 199);")
        self.defaultButtonTab2.setObjectName("defaultButtonTab2")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.othersTab)
        self.buttonBox_2.setGeometry(QtCore.QRect(125, 355, 166, 24))
        self.buttonBox_2.setStyleSheet("color: rgb(199, 199, 199);")
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.tabbedConfig.addTab(self.othersTab, "")
        self.rosMyIPLabel.setBuddy(self.myIP)
        self.rosMasterIPLabel.setBuddy(self.masterIP)
        self.rosHostnameLabel.setBuddy(self.hostname)
        self.rosNamespaceLabel.setBuddy(self.nameSpace)
        self.rosMasterIURILabel.setBuddy(self.masterURI)
        # self.portLabel.setBuddy(self.port)
        # self.userLabel.setBuddy(self.user)
        # self.passwordLabel.setBuddy(self.password)
        # self.turtlebotIPLabel.setBuddy(self.turtlebotIP)
        # self.perspectiveLabel.setBuddy(self.myIP)
        # self.rosSourceLabel.setBuddy(self.masterIP)
        # self.rosETCDirectoryLabel.setBuddy(self.hostname)
        # self.rosRootLabel.setBuddy(self.nameSpace)
        self.retranslateUi(envConfigDialog)
        self.tabbedConfig.setCurrentIndex(0)
        # OK e CANCEL da TAB 1
        self.buttonBox.accepted.connect(self.okButton)
        self.buttonBox.rejected.connect(self.reject)
        self.defaultButton.clicked.connect(self.defaultXML)
        # OK e CANCEL da TAB 2
        # self.buttonBox_2.accepted.connect(self.okButton)
        # self.buttonBox_2.rejected.connect(self.reject)
        # self.defaultButtonTab2.clicked.connect(self.defaultXML)
        # COPY
        self.buttonBox.accepted.connect(self.myIP.copy)
        self.buttonBox.accepted.connect(self.masterIP.copy)
        self.buttonBox.accepted.connect(self.hostname.copy)
        self.buttonBox.accepted.connect(self.nameSpace.copy)
        # self.buttonBox.accepted.connect(self.turtlebotIP.copy)
        # self.buttonBox.accepted.connect(self.user.copy)
        # self.buttonBox.accepted.connect(self.password.copy)
        # self.buttonBox.accepted.connect(self.port.copy)
        self.buttonBox.accepted.connect(self.masterURI.copy)
        # self.buttonBox_2.accepted.connect(self.perspective.copy)
        # self.buttonBox_2.accepted.connect(self.rosSource.copy)
        # self.buttonBox_2.accepted.connect(self.rosETCDirectory.copy)
        # self.buttonBox_2.accepted.connect(self.rosRoot.copy)
        # RESET
        self.defaultButton.clicked.connect(self.masterIP.redo)
        self.defaultButton.clicked.connect(self.hostname.redo)
        self.defaultButton.clicked.connect(self.nameSpace.redo)
        # self.defaultButton.clicked.connect(self.turtlebotIP.redo)
        # self.defaultButton.clicked.connect(self.user.redo)
        # self.defaultButton.clicked.connect(self.password.redo)
        # self.tabbedConfig.currentChanged['int'].connect(self.port.redo)
        # self.defaultButtonTab2.clicked.connect(self.perspective.redo)
        # self.defaultButtonTab2.clicked.connect(self.rosSource.redo)
        # self.defaultButtonTab2.clicked.connect(self.rosETCDirectory.redo)
        # self.defaultButtonTab2.clicked.connect(self.rosRoot.redo)
        QtCore.QMetaObject.connectSlotsByName(envConfigDialog)
        self.show()
        self.exec_()


    #shutdown function 
    def shutdownButtonstate(self):

        self.shutdownButton.setDown(True)
        print('Shutting Down the Turtlebot...')
        #QTimer.singleShot(5000, lambda: self.robotDownButton.setDown(False))
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
        
    def restartButton_procc(self):
        print('Starting the ROS...')
        #QTimer.singleShot(5000, lambda: self.robotStartButton.setDown(False))
        # For localserver use this code:
       
        minimalLaunch = 'roscore '
       
        # kinectLaunch = 'roslaunch turtlebot_bringup 3dsensors.launch'
        # Using Popen instead of Call because the first one don't block the process
        launchProcess = subprocess.Popen(minimalLaunch, stdout=PIPE,
                                            stdin=PIPE, shell=True)
    def okButton(self):
        # ENV CONFIG
        myIPValue = self.myIP.text()
        masterIPValue = self.masterIP.text()
        masterURIValue = self.masterURI.text()
        hostnameValue = self.hostname.text()
        nameSpaceValue = self.nameSpace.text()
        # SSH CONNECTION
        # turtlebotIPValue = self.turtlebotIP.text()
        # userValue = self.user.text()
        # passwordValue = self.password.text()
        # portValue = self.port.text()
        # PERSPECTIVE AND OTHERS
        # perspectiveValue = self.perspective.text()
        # rosSourceValue = self.rosSource.text()
        # rosEtcDirectoryValue = self.rosETCDirectory.text()
        # rosRootValue = self.rosRoot.text()
        # XML CREATION
        environmentXMLFile = et.Element('environment')
        comment = et.Comment("Python Environment and Configuration Values")
        environmentXMLFile.append(comment)
        environmentConfig = et.SubElement(environmentXMLFile, 'MY_IP')
        environmentConfig.text = str(myIPValue)
        environmentConfig = et.SubElement(environmentXMLFile, 'MASTER_IP')
        environmentConfig.text = str(masterIPValue)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROS_MASTER_URI')
        environmentConfig.text = str(masterURIValue)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROS_HOSTNAME')
        environmentConfig.text = str(hostnameValue)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROS_NAMESPACE')
        environmentConfig.text = str(nameSpaceValue)
        environmentConfig = et.SubElement(environmentXMLFile, 'TURTLEBOT_IP')
        # environmentConfig.text = str(turtlebotIPValue)
        # environmentConfig = et.SubElement(environmentXMLFile, 'USERNAME')
        # environmentConfig.text = str(userValue)
        # environmentConfig = et.SubElement(environmentXMLFile, 'PASSWORD')
        # environmentConfig.text = str(passwordValue)
        # environmentConfig = et.SubElement(environmentXMLFile, 'PORT')
        # environmentConfig.text = str(portValue)
        # environmentConfig = et.SubElement(environmentXMLFile, 'PERSPECTIVE_LOCATION')
        # environmentConfig.text = str(perspectiveValue)
        # environmentConfig = et.SubElement(environmentXMLFile, 'ROS_SOURCE')
        # environmentConfig.text = str(rosSourceValue)
        # environmentConfig = et.SubElement(environmentXMLFile, 'ROS_ETC_DIRECTORY')
        # environmentConfig.text = str(rosEtcDirectoryValue)
        # environmentConfig = et.SubElement(environmentXMLFile, 'ROS_ROOT')
        # environmentConfig.text = str(rosRootValue)
        tree = et.ElementTree(environmentXMLFile)
        tree.write('environment.xml', encoding='utf8')
        # Reads the XML File
        xmlFile = et.parse('environment.xml')
        # Find the root element from the file (in this case "environment")
        root = xmlFile.getroot()
        # Load the XML values from environment file
        myIP = root.findtext('MY_IP')
        masterIP = root.findtext('MASTER_IP')
        rosMasterURI = root.findtext('ROS_MASTER_URI')
        rosHostname = root.findtext('ROS_HOSTNAME')
        rosNamespace = root.findtext('ROS_NAMESPACE')
        address = root.findtext('TURTLEBOT_IP')
        usernameClient = root.findtext('USERNAME')
        passwordClient = root.findtext('PASSWORD')
        portClient = root.findtext('PORT')
        # perspectiveLocation = root.findtext('PERSPECTIVE_LOCATION')
        # rosSource = root.findtext("ROS_SOURCE")
        # rosEtc = root.findtext('ROS_ETC_DIRECTORY')
        # rosRoot = root.findtext('ROS_ROOT')
        exportMyIP = str('export ROS_MY_IP='+myIP)
        exportMasterIP = str('export ROS_MASTER_IP='+masterIP)
        exportMasterIPURI = str('export ROS_MASTER_URI='+rosMasterURI)
        exportHostname = str('export ROS_HOSTNAME='+myIP)
        exportNamespace = str('export ROS_NAMESPACE='+rosNamespace)
        # Export the values to "~/.bashrc"
        exportMyIPCommand = str("echo '"+exportMyIP+"' >> ~/.bashrc")
        exportMasterIPCommand = str("echo '"+exportMasterIP+"' >> ~/.bashrc")
        exportIPURICommand = str("echo '"+exportMasterIPURI+"' >> ~/.bashrc")
        exportHostnameCommand = str("echo '"+exportHostname+"' >> ~/.bashrc")
        exportNamespaceCommand = str("echo '"+exportNamespace+"' >> ~/.bashrc")

        print(exportMyIPCommand)
        print(exportMasterIPCommand)
        print(exportIPURICommand)
        print(exportHostnameCommand)
        print(exportNamespaceCommand)

        exportMyIPProcess = subprocess.Popen(exportMyIPCommand, stdout=PIPE,
                                             stdin=PIPE, shell=True)
        exportMasterIPProcess = subprocess.Popen(exportMasterIPCommand, stdout=PIPE,
                                                 stdin=PIPE, shell=True)
        exportIPURIProcess = subprocess.Popen(exportIPURICommand, stdout=PIPE,
                                              stdin=PIPE, shell=True)
        exportHostnameProcess = subprocess.Popen(exportHostnameCommand, stdout=PIPE,
                                                 stdin=PIPE, shell=True)
        exportNamespaceProcess = subprocess.Popen(exportNamespaceCommand, stdout=PIPE,
                                                 stdin=PIPE, shell=True) 
        # Closes the Configuration Menu
        self.close()

    def defaultXML(self):
        # ENV CONFIG
        myIPValueDefault = str('150.165.167.105')
        masterIPValueDefault = str('150.165.167.105')
        masterURIValueDefault = str('http://localhost:11311')
        hostnameValueDefault = str('localhost')
        nameSpaceValueDefault = str('robot_0')
        # SSH CONNECTION
        turtlebotIPValueDefault = str(myIPValueDefault)
        userValueDefault = 'turtlebot'
        passwordValueDefault = 'turtlebot'
        portValueDefault = '22'
        # PERSPECTIVE AND OTHERS
        # perspectiveValueDefault = self.perspective.text()
        # rosSourceValueDefault = self.rosSource.text()
        # rosEtcDirectoryValueDefault = self.rosETCDirectory.text()
        # rosRootValueDefault = self.rosRoot.text()
        environmentXMLFile = et.Element('environment')
        comment = et.Comment("Python Environment and Configuration Values")
        environmentXMLFile.append(comment)
        environmentConfig = et.SubElement(environmentXMLFile, 'MY_IP')
        environmentConfig.text = str(myIPValueDefault)
        environmentConfig = et.SubElement(environmentXMLFile, 'MASTER_IP')
        environmentConfig.text = str(masterIPValueDefault)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROS_MASTER_URI')
        environmentConfig.text = str(masterURIValueDefault)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROS_HOSTNAME')
        environmentConfig.text = str(hostnameValueDefault)
        environmentConfig = et.SubElement(environmentXMLFile, 'ROS_NAMESPACE')
        environmentConfig.text = str(nameSpaceValueDefault)
        environmentConfig = et.SubElement(environmentXMLFile, 'TURTLEBOT_IP')
        environmentConfig.text = str(turtlebotIPValueDefault)
        environmentConfig = et.SubElement(environmentXMLFile, 'USERNAME')
        environmentConfig.text = str(userValueDefault)
        environmentConfig = et.SubElement(environmentXMLFile, 'PASSWORD')
        environmentConfig.text = str(passwordValueDefault)
        environmentConfig = et.SubElement(environmentXMLFile, 'PORT')
        environmentConfig.text = str(portValueDefault)
        # environmentConfig = et.SubElement(environmentXMLFile, 'PERSPECTIVE_LOCATION')
        # environmentConfig.text = str(perspectiveValueDefault)
        # environmentConfig = et.SubElement(environmentXMLFile, 'ROS_SOURCE')
        # environmentConfig.text = str(rosSourceValueDefault)
        # environmentConfig = et.SubElement(environmentXMLFile, 'ROS_ETC_DIRECTORY')
        # environmentConfig.text = str(rosEtcDirectoryValueDefault)
        # environmentConfig = et.SubElement(environmentXMLFile, 'ROS_ROOT')
        # environmentConfig.text = str(rosRootValueDefault)
        tree = et.ElementTree(environmentXMLFile)
        tree.write('environment.xml', encoding='utf8')
        # Reads the XML File
        xmlFile = et.parse('environment.xml')
        # Find the root element from the file (in this case "environment")
        root = xmlFile.getroot()
        # Load the XML values from environment file
        myIP = root.findtext('MY_IP')
        masterIP = root.findtext('MASTER_IP')
        rosMasterURI = root.findtext('ROS_MASTER_URI')
        rosHostname = root.findtext('ROS_HOSTNAME')
        rosNamespace = root.findtext('ROS_NAMESPACE')
        address = root.findtext('TURTLEBOT_IP')
        usernameClient = root.findtext('USERNAME')
        passwordClient = root.findtext('PASSWORD')
        portClient = root.findtext('PORT')
        perspectiveLocation = root.findtext('PERSPECTIVE_LOCATION')
        rosSource = root.findtext("ROS_SOURCE")
        rosEtc = root.findtext('ROS_ETC_DIRECTORY')
        rosRoot = root.findtext('ROS_ROOT')
        # Values to Export into "~/.bashrc" 
        # exportIP = str('MY_IP='+myIP)
        # exportMasterIP = str('MASTER_IP='+myIP)
        exportMasterIPURI = str('export ROS_MASTER_URI='+rosMasterURI)
        exportRosIP = str('export ROS_IP='+myIP)
        exportHostname = str('export ROS_HOSTNAME='+rosHostname)
        exportNamespace = str('export ROS_NAMESPACE='+rosNamespace)
        # Export the values to "~/.bashrc"
        exportIPURICommand = str("echo "+exportMasterIPURI+" >> ~/.bashrc")
        exportRosIPCommand = str("echo "+exportRosIP+" >> ~/.bashrc")
        exportHostnameCommand = str("echo "+exportHostname+" >> ~/.bashrc")
        exportNamespaceCommand = str("echo "+exportNamespace+" >> ~/.bashrc")
        print(exportIPURICommand)
        print(exportRosIPCommand)
        print(exportHostnameCommand)
        print(exportNamespaceCommand)
        # Using Popen instead of Call because the first one don't block the process
        exportURIProcess = subprocess.Popen(exportIPURICommand, stdout=PIPE,
                                            stdin=PIPE, shell=True)
        exportRosIPProcess = subprocess.Popen(exportRosIPCommand, stdout=PIPE,
                                              stdin=PIPE, shell=True)
        exportHostnameProcess = subprocess.Popen(exportHostnameCommand, stdout=PIPE,
                                                 stdin=PIPE, shell=True)
        exportNamespaceProcess = subprocess.Popen(exportNamespaceCommand, stdout=PIPE,
                                                 stdin=PIPE, shell=True) 
        # Closes the Configuration Menu
        self.close()

    def retranslateUi(self, envConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        envConfigDialog.setWindowTitle(_translate("envConfigDialog", "Settings"))
        self.envConfigTab.setTitle(_translate("envConfigDialog", "Environment Variables:"))
        self.myIP.setPlaceholderText(_translate("envConfigDialog", "ex.:192.168.43.87"))
        self.masterIP.setPlaceholderText(_translate("envConfigDialog", "ex.: 192.168.43.87"))
        self.hostname.setPlaceholderText(_translate("envConfigDialog", "ex.:192.168.43.87"))
        self.nameSpace.setPlaceholderText(_translate("envConfigDialog", "robot_0"))
        self.rosMyIPLabel.setText(_translate("envConfigDialog", "ROS_MY_IP:"))
        self.rosMasterIPLabel.setText(_translate("envConfigDialog", "MASTER_IP:"))
        self.rosHostnameLabel.setText(_translate("envConfigDialog", "HOSTNAME:"))
        self.rosNamespaceLabel.setText(_translate("envConfigDialog", "NAMESPACE:"))
        self.rosMasterIURILabel.setText(_translate("envConfigDialog", "MASTER_URI:"))
        self.masterURI.setPlaceholderText(_translate("envConfigDialog", "http://localhost:11311"))
        # self.groupBox_2.setTitle(_translate("envConfigDialog", "SSH Configuration:"))
        # self.user.setPlaceholderText(_translate("envConfigDialog", "turtlebot"))
        # self.password.setPlaceholderText(_translate("envConfigDialog", "turtlebot"))
        # self.portLabel.setText(_translate("envConfigDialog", "PORT:"))
        # self.port.setPlaceholderText(_translate("envConfigDialog", "80"))
        # self.userLabel.setText(_translate("envConfigDialog", "USER:"))
        # self.turtlebotIP.setPlaceholderText(_translate("envConfigDialog", "192.168.43.87"))
        # self.passwordLabel.setText(_translate("envConfigDialog", "PASSWORD:"))
        # self.turtlebotIPLabel.setText(_translate("envConfigDialog", "TURTLEBOT IP:"))
        self.defaultButton.setText(_translate("envConfigDialog", "Default"))
        self.tabbedConfig.setTabText(self.tabbedConfig.indexOf(self.connectionConfig), _translate("envConfigDialog", "ROS Connection"))
        # self.rosSource.setPlaceholderText(_translate("envConfigDialog", "ex.:/opt/ros/<distro>/setup.bash"))
        # self.perspectiveLabel.setText(_translate("envConfigDialog", "Perspective:"))
        # self.perspective.setPlaceholderText(_translate("envConfigDialog", "ex.:/config/test.perspective"))
        # self.rosETCDirectory.setPlaceholderText(_translate("envConfigDialog", "ex.:/opt/ros/indigo/etc/ros"))
        # self.rosSourceLabel.setText(_translate("envConfigDialog", "ROS_SOURCE:"))
        # self.rosETCDirectoryLabel.setText(_translate("envConfigDialog", "ROS_ETC:"))
        # self.rosRoot.setPlaceholderText(_translate("envConfigDialog", "ex.:/opt/ros/indigo/share/ros"))
        # self.rosRootLabel.setText(_translate("envConfigDialog", "ROS_ROOT:"))
        self.defaultButtonTab2.setText(_translate("envConfigDialog", "Default"))
        self.tabbedConfig.setTabText(self.tabbedConfig.indexOf(self.othersTab), _translate("envConfigDialog", "About Spark"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    config = settings()
    config.show()
    sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()
