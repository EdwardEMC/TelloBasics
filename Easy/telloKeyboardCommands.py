# PILOTING A DRONE WITH THE USE OF KEYBOARD COMMANDS
# KEYBOARD INPUT IS CONTROLLED THROUGH THE KEY BOARD MODULE

from djitellopy import Tello
import keyboardModule as kp
import time

kp.init()
# CONNECTING TO THE DRONE
drone = Tello() # creates a tello object
drone.connect() # connects to the drone, auto connects through ip address
print(drone.get_battery()) # print out the battery status

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
    if kp.getKey("q"): drone.land()

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    time.sleep(0.05) # keep things stable