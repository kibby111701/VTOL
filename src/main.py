'''main executable for setting up VTOL'''
import json
from dronekit import LocationGlobalRelative
from vtol import setup_vehicle

def main(configs):
    '''Configure vtol and ready for mission'''
    vehicle = setup_vehicle(configs)
    vehicle.takeoff()
    # vehicle.send_ned_velocity(-5, 3, 0, 5)
    vehicle.set_attitude(pitch_angle=20, duration=5)

    vehicle.takeoff()

    home = vehicle.location.global_relative_frame

    destination = LocationGlobalRelative(configs["dest"]["lat"],\
        configs["dest"]["long"],\
        configs["dest"]["alt"])

    vehicle.go_to(destination)
    # Pick-up function for ping pong balls

    vehicle.land()

    vehicle.takeoff()

    vehicle.go_to(home)

    vehicle.land()

if __name__ == '__main__':
    with open('configs.json', 'r') as data:
        main(json.load(data))
