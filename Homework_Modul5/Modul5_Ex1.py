""" Homework 5 - needs to be presented before exam day"""

# We want to create class for an object that behaves like a triangle, that has flexible sides and angles.
# Because of approximations in python the triangle will get distorted after some of the changes so this is not a
# perfect model

# 30P
#  - class constructor can receive 3 arguments for angles (with default value of 60) and 3 arguments for sides (with
# default value of 1)
# class variables for sides will be called A, B, C
# class variables for angles will be called AB, BC, CA (indicating sides)

# 30P
# - class implements method to modify_angle:
#   - modify_angle method takes two argument:
#       - "angle" and can be one of 3 string values 'AB', 'BC', 'CA'
#       - "degrees" that can be a positive or negative and represents the amount by which the angle will be modified
# If as a result of the change any of the angles will be outside interval (0, 180) then method should raise an exception
# When an angle is modifies you will need to recalculate the opposing side which can be done using the following
# example: angle AB is changed then C = (A**2 + B**2 - 2*A*B*cos(AB))**(1/2)
# Because angles in a triangle must sum up to 180 degrees unmodified angles need to be recalculated after we have
# recalculated the opposite side using the following example:
# angle AB is changed then BC = arccos((B**2+ C**2 - A**2) / 2*B*C), CA = arccos((C**2+ A**2 - B**2) / 2*C*A),



from math import cos, acos

class AngleIsInconsistent(ValueError):
    '''exception class when the angle is below 0 or above 180 '''
    pass

class Triangle():

    def __init__(self,A=1,B=1,C=1,AB=60,BC=60,CA=60):
        self.A = A
        self.B = B
        self.C = C
        self.AB = AB
        self.BC = BC
        self.CA = CA

    def modify_angle(self,angle,degrees):
        angle = angle + degrees
        if(angle < 0 or angle > 180):
            raise AngleIsInconsistent(angle)



