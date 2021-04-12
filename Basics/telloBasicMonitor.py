## IMPORTANT DRONE CONNECTION TO WIFI DEVICE MUST BE PRIVATE ##
from djitellopy import Tello # connection to the drone
import time # waiting between tasks
import cv2
from cv2 import cv2

####################################################
width = 320         # WIDTH of the image
height = 240        # HEIGHT of the image
startCounter = 0    # 0 for flight 1 for testing
####################################################

# CONNECT TO TELLO
drone = Tello()
drone.connect()
drone.for_back_velocity = 0
drone.left_right_velocity = 0
drone.up_down_velocity = 0
drone.yaw_velocity = 0
drone.speed = 0

print(drone.get_battery())

drone.streamoff()
drone.streamon()

while True:
    
    # GET THE IMAGE FROM TELLO
    frame_read = drone.get_frame_read()
    myFrame = frame_read.frame
    print(myFrame)
    img = cv2.resize(myFrame, (width, height))

    # TO GO UP IN THE BEGINNING (TAKE OFF)
    if startCounter == 0:
        drone.takeoff()
        time.sleep(8) # needs time to execute the take off
        drone.rotate_clockwise(90)
        startCounter = 1

    # DISPLAY IMAGE
    cv2.imshow("MyResult", img)

    # WAIT FOR THE 'Q' BUTTON TO STOP
    # MUST HAVE THE IMAGE WINDOW AS THE ACTIVE WINDOW TO REGISTER THE KEYPRESS
    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land()
        cv2.destroyAllWindows()
        break
