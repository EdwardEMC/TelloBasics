## IMPORTANT DRONE CONNECTION TO WIFI DEVICE MUST BE PRIVATE ##
# CAPTURING THE IMAGE FROM THE DRONES CAMERA

from djitellopy import Tello
import time
import cv2
from cv2 import cv2

# CONNECTING TO THE DRONE
drone = Tello() # creates a tello object
drone.connect() # connects to the drone, auto connects through ip address

print(drone.get_battery()) # print out the battery status

drone.streamon() # turning the stream on, contiuously sends frames

while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img, 360, 240) # resize the image for a faster load rate

    cv2.imshow("Image", img) # creates a window to view the new image imshow(window name, image to view)
    
    # cv2.waitKey(1) wait one milisecond so the frame isn't discarded right away
    # WAIT FOR THE 'Q' BUTTON TO STOP
    # MUST HAVE THE IMAGE WINDOW AS THE ACTIVE WINDOW TO REGISTER THE KEYPRESS
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break