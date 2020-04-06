import time
from dronekit import connect, VehicleMode, LocationGlobalRelative

#__ connect to vehicle
#import argparse
#parser = argparse.ArgumentParser(description='commands')
#parser.add_argument(("--connect")
#args = parser.parse_args()

#connection_string = args.connect

#print("Connection to the vehicle on %s"%connection_string)
vehicle = connect('udp:127.0.0.1:2346',wait_ready=True)

#__ define the function for takeoff

#time.sleep(5)

print("Arming motors")
while not vehicle.is_armable:
    time.sleep(1)

vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True

 #vehicle.airspeed = 7

print('Takeoff')

vehicle.simple_takeoff(25)

while True:
    altitude = vehicle.location.global_relative_frame.alt
    print(altitude)
    if altitude >= 24:
        print("altitude_reached")
	break
    time.sleep(1)



vehicle.mode = vehicleMode("RTL")

time.sleep(20)
vehicle.mode = VehicleMode("STABILIZE")

vehicle.close()

