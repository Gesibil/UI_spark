# TurtleUI

A Generic Graphical User Interface for Robot Control

This work presents a graphical interface developed through the PyQt framework, focused on robots equipped with Robot Operating System (ROS) framework and designed with ease for starting processes. it integrates the face recognition module used in the authentification access and in the module of speaking to a known person.


## Libraries Used

- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
- [ROS melodic](https://www.ros.org/)
- [OpenCV](https://opencv.org/)
- [face recognition](https://pypi.org/project/face-recognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)


## User manual

The main folder contains the following scripts:

SparkScreen.py: This script is responsible for running the user interface (UI) of the application.

``` shell
python3 SparkScreen.py  
```
##

Salut.py: This script is designed to greet known individuals by saying "Hi."

``` shell
python3 Salut.py  
```
##
Spark.py: This script utilizes multithread technology to simultaneously run both the SparkScreen.py and Salut.py scripts.
``` shell
python3 Spark.py  
```
##
Additionally, there is a file called Settings.py which is associated with the main SparkScreen.py script. This file likely contains configuration settings or variables 
specific to the functionality of the UI.

For more detailed information on the functionality and usage of each script, please refer to their individual files.


