import math

def cone_volume(radius, height):
    return math.pi * radius**2 * height / 3

radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

volume = cone_volume(radius, height)

print("Volume of the cone is:", volume)
