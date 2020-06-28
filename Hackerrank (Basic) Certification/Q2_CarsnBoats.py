#!/bin/python3

import math
import os
import random
import re
import sys



class Car:

    speed = None
    unit = None

    def __init__(self, speed, unit):
        self.speed = speed
        self.unit = unit
        
    def __new__(self, speed, unit):
        self.speed = speed
        self.unit = unit
        return "Car with the maximum speed of " + str(self.speed) + " " + self.unit 


class Boat:

    speed = None

    def __init__(self, speed):
        self.speed = speed

    def __new__(self, speed):
        self.speed = speed
        return "Boat with the maximum speed of " + str(self.speed) + " knots"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()
