'''main executable for setting up VTOL'''
import json
from util import setup_vehicle
from quad import QUAD

def main(configs):
    '''Configure vtol and ready for mission'''
    vehicle = setup_vehicle(configs, QUAD)
    vehicle.takeoff()

if __name__ == '__main__':
    with open('configs.json', 'r') as data:
        main(json.load(data))