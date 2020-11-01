###    Write a program to calculate the volume and surface area of a sphere from
###    its radius, given as input.

def f():
    import math
    print ("The following program calculates the volume and surface area of a sphere")
    while True:
        user_input_radius = float(input("Enter radius of the sphere [in metres]:"))
        if (user_input_radius > 0) :
            volume_sphere = (4/3) * (math.pi) * (user_input_radius ** 3)
            surface_area_sphere = 4 * (math.pi) * (user_input_radius**2)
            print ("The volume of the sphere is :", volume_sphere, " cubic metres")
            print ("The area of the sphere is :", surface_area_sphere, " metre squares")
        else :
            print ("The radius of a sphere can not be negative. Please type another value")
