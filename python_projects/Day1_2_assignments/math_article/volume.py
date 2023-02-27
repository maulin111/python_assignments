import math


def volume_of_sphere(radius):
    result = 4/3 * 3.14 * radius * radius
    return result

def volume_of_cylinder(radius,height):
    result = math.pi * radius * radius * height
    return result
