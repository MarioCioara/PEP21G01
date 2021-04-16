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

# 30P
# - class implements method to modify_side:
#   - modify_side method takes two argument:
#       - "side" and can be one of 3 string values 'A', 'B', 'C'
#       - "meters" that can be a positive or negative and represents the amount by which the side will be modified
# If as a result of the change sum of the unmodified sides is less than or equal to the changed side then method should
# throw an exception
# If as a result of the change side will be less than or equal to 0 then method should raise a different exception
# When a side is modified by some value all other sides need to be modified by the fraction of the change to maintain
# the same triangle angles. For example, if A increase by +1 then B = ((A+1)/A)*B and C = ((A+1)/A)*C



#Pentru calcularea celui de-al treilea unghi am scazut din 180 primele doua unghiuri deoarece daca utilizam formula din exercitiu
#atunci unghiurile 2 si 3 erau egale,iar suma celor 3 unghiuri nu mai era 180

from math import cos, acos
from math import degrees as grade


class Triangle():

    def __init__(self,A=60,B=60,C=60,AB=1,BC=1,CA=1): #angle 1,2,3 & side 1,2,3
        self.A = BC
        self.B = CA
        self.C = AB
        self.AB = C
        self.BC = A
        self.CA = B

    def modify_angle(self,angle,degrees):
        self.angle = angle

        if self.angle == 'AB':
            self.AB = self.AB + degrees
            if (self.AB <= 0) or (self.AB >= 180):
                raise Exception("Angle is inappropriate")
            else:
                self.C = (self.A ** 2 + self.B ** 2 - 2 * self.A * self.B * cos(self.AB))**(1/2)
                self.BC = grade(acos((self.B ** 2 + self.C ** 2 - self.A ** 2) / (2 * self.B * self.C)))
                self.CA = 180 - self.AB - self.BC

        elif self.angle == 'BC':
            self.BC = self.BC + degrees
            if (self.BC <= 0) or (self.BC >= 180):
                raise Exception("Angle is inappropriate")
            else:
                self.A = (self.B ** 2 + self.C ** 2 - 2 * self.B * self.C * cos(self.BC))**(1/2)
                self.CA = grade(acos((self.C ** 2 + self.A ** 2 - self.B ** 2) / (2 * self.C * self.A)))
                self.AB = 180 - self.BC - self.CA

        elif self.angle == 'CA':
            self.CA = self.CA + degrees
            if (self.CA <= 0) or (self.CA >= 180):
                raise Exception("Angle is inappropriate")
            else:
                self.B = (self.C ** 2 + self.A ** 2 - 2 * self.C * self.A * cos(self.CA)**(1/2))
                self.AB = grade(acos((self.A ** 2 + self.B ** 2 - self.C ** 2) / (2 * self.A * self.B)))
                self.BC = 180 - self.AB - self.CA
        else:
             raise Exception("Please insert AB,BC or CA")
        print(f"Triangle's sides are : {self.A, self.B, self.C},")
        print(f"Triangle's angles are: {self.BC, self.CA, self.AB}")

    def modify_side(self, side, meters):
        self.side = side

        if self.side == 'A':
            self.A = self.A + meters
            self.B = ((self.A + meters) / self.A) * self.B
            self.C = ((self.A + meters) / self.A) * self.C
            if (self.A + self.B < self.C) or (self.B + self.C < self.A) or (self.C + self.A < self.B):
                raise Exception("The length is inappropriate")
            elif (self.A <= 0) or (self.B <= 0) or (self.C <= 0):
                raise Exception("The side length should be above zero")

        elif self.side == 'B':
            self.B = self.B + meters
            self.C = ((self.B + meters) / self.B) * self.C
            self.A = ((self.B + meters) / self.B) * self.A
            if (self.B + self.C < self.A) or (self.C + self.A < self.B) or (self.A + self.B < self.C):
                raise Exception("The length is inappropriate")
            elif (self.B <= 0) or (self.C <= 0) or (self.A <= 0):
                raise Exception("The side length should be above zero")

        elif self.side == 'C':
            self.C = self.C + meters
            self.A = ((self.C + meters) / self.C) * self.A
            self.B = ((self.C + meters) / self.C) * self.B
            if (self.B + self.C < self.A) or (self.C + self.A < self.B) or (self.A + self.B < self.C):
                raise Exception("The length is inappropriate")
            elif (self.C <= 0) or (self.A <= 0) or (self.C <= 0):
                raise Exception("The side length should be above zero")

        return print("The triangle's new sides length are: ", self.A, self.B, self.C)

obj_triangle = Triangle(60, 60, 60, 1, 1, 1)
print()
obj_triangle.modify_angle("AB", 30)
print()
obj_triangle.modify_side("A", 1.5)




