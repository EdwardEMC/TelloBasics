## IMPORTANT DRONE CONNECTION TO WIFI DEVICE MUST BE PRIVATE ##
# FLYING A DRONE WITH KEYBOARD INPUTS VIA A VIDEO STREAM
# TAKING PHOTOS WITH A KEYPRESS 'p'

from djitellopy import Tello
import keyboardModule as kp
import time
import cv2
from cv2 import cv2

kp.init()
# CONNECTING TO THE DRONE
drone = Tello() # creates a tello object
drone.connect() # connects to the drone, auto connects through ip address
print(drone.get_battery()) # print out the battery status
global img # global variable for the current frame of the video stream
drone.streamon() # turning the stream on, contiuously sends frames

# FLIGHT CONTROLS
def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0 # leftright, forwardsbackwards, updown, yawvelocity
    speed = 50 # constant value for velocity

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey("e"): drone.takeoff()
    if kp.getKey("l"): drone.land()

    if kp.getKey("p"): # save an image
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img) # save img with a time stamp so no two files are the same
        time.sleep(0.3) # add a delay so that only one image is captured

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (360, 240)) # resize the image for a faster load rate

    cv2.imshow("Image", img) # creates a window to view the new image imshow(window name, image to view)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break