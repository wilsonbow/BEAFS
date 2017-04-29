"""
Source code for the engineering classes and functions in BEAFS.
"""

from math import sqrt
from math import acos

__author__ = "Wilson G. Bow"


class Vector:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "<{}, {}, {}>".format(self.x, self.y, self.z)

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def angles(self):
        x_theta = acos(self.x / self.magnitude())
        y_theta = acos(self.y / self.magnitude())
        z_theta = acos(self.z / self.magnitude())
        return [x_theta, y_theta, z_theta]

    def unit_vector(self):
        unit_x = self.x / self.magnitude()
        unit_y = self.y / self.magnitude()
        unit_z = self.z / self.magnitude()
        return Vector(unit_x, unit_y, unit_z)


def dot_product(v1: Vector, v2: Vector):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z


def cross_product(v1: Vector, v2: Vector):
    v_ans = Vector()
    v_ans.x = v1.y * v2.z - v2.y * v1.z
    v_ans.y = v2.x * v1.z - v1.x * v2.z
    v_ans.z = v1.x * v2.y - v2.x * v1.y
    return v_ans
