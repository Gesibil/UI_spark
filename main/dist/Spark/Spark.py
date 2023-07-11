import threading
import subprocess
camera_lock = threading.Lock()
# Define a function to run your PyQt5 interface
def run_interface():
   #subprocess.call(['python3', '/home/ubuntu/spark_int/TurtleUI-master/main/SparkScreen.py'])
    subprocess.call(['python3', '/home/ubuntu/TurtleUI-master/main/SparkScreen.py'])
    
# Define a function to run your face recognition script
def run_face_recognition():
   
  # subprocess.call(['python3', '/home/ubuntu/spark_int/TurtleUI-master/main/testcam.py'])
   
   subprocess.call(['python3', '/home/ubuntu/TurtleUI-master/main/testcam.py'])
   
# Create two threads for each script
t1 = threading.Thread(target=run_interface)
t2 = threading.Thread(target=run_face_recognition)

# Start both threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()
