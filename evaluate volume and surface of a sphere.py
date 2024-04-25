import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def sphere_surface(radius):
    return 4 * math.pi * radius**2

radius = float(input("Enter the radius of the sphere: "))

volume = sphere_volume(radius)
surface = sphere_surface(radius)

print("Volume of the sphere is:", volume)
print("Surface area of the sphere is:", surface)
