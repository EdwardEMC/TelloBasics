## IMPORTANT DRONE CONNECTION TO WIFI DEVICE MUST BE PRIVATE ##
# CONTROLLING A DRONE'S MOVEMENT USING VELOCITY AND DISTANCE

from djitellopy import Tello
import time

# CONNECTING TO THE DRONE
drone = Tello() # creates a tello object
drone.connect() # connects to the drone, auto connects through ip address

print(drone.get_battery()) # print out the battery status

# CRT + *click* takeoff() or any other command to get all drone commands

# Controlling the drone's movement through velocity - constant movement
drone.takeoff()
drone.send_rc_control(0, 20, 0, 0) # send_rc_control(left-right, forward-backwards, up-down, yaw). (values between -100 ~ 100)
time.sleep(2) # wait for the previous execution to finish, if not enough time is provided the next execution may be skipped
drone.send_rc_control(20, 0, 0, 0)
time.sleep(2)
drone.send_rc_control(0, 0, 0, 0) # stop all velocity
drone.land()

# Controlling the drone's movement through distance
drone.takeoff()
drone.move_forward(10) # fly forward 10cm
time.sleep(4)
drone.move_right(10) # fly right 10cm
time.sleep(4)
drone.land()