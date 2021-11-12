import math
print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
print("§                  Stiv Llenga                   §")
print("§           PhD student of CCC group             §")
print("§  Heidelbeg Institute for Theoretical Sciences  §")
print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
print()
print("This program is created to find the equation of the molecular plane, mainly used to check the BFPI values.")
print()
print("Please follow each instruction rigorously...")
print()
print("Finding the equation of the plane created from three points in space...")
print()
a1 = float(input("Add the value of x of the fist point (the origin of the vectors):\n"))   # This point is the x of the origin of each vector
a2 = float(input("Add the value of y of the fist point (the origin of the vectors):\n"))   # This point is the y of the origin of each vector
a3 = float(input("Add the value of z of the fist point (the origin of the vectors):\n"))   # This point is the z of the origin of each vector
b1 = float(input("Add the value of x of the second point (the head of the first vector):\n"))  # This point is the x of the head of vector 12
b2 = float(input("Add the value of y of the second point (the head of the first vector):\n"))  # This point is the y of the head of vector 12
b3 = float(input("Add the value of z of the second point (the head of the first vector):\n"))  # This point is the z of the head of vector 12
c1 = float(input("Add the value of x of the third point (the head of the second vector):\n"))  # This point is the x of the head of vector 13
c2 = float(input("Add the value of y of the third point (the head of the second vector):\n"))  # This point is the y of the head of vector 13
c3 = float(input("Add the value of z of the third point (the head of the second vector):\n"))  # This point is the y of the head of vector 13
x12 = b1-a1
y12 = b2-a2
z12 = b3-a3
x13 = c1-a1
y13 = c2-a2
z13 = c3-a3
A = float(y12*z13-y13*z12)
B = float(x12*z13-x13*z12)
C = float(x12*y13-y12*x13)
D = float(A*a1+B*a2+C*a3)
print(f"The equation of the plane is: {A} x + {B} y + {C} z = {D} ")
print()
print()
print("Finding the distance of a point (x1;y1;z1) from our plane...")
while True:
    print("Calculating the distance of your point from this plane...")
    print()
    x1 = float(input("Add the x of your point: "))
    y1 = float(input("Add the y of your point: "))
    z1 = float(input("Add the z of your point: "))
    dist = abs(A*x1+B*y1+C*z1-D)/math.sqrt(A*A+B*B+C*C)
    print()
    print(f"The distance of ({x1} ; {y1} ; {z1}) from plane {A} x + {B} y + {C} z = {D} is : {dist}" )
    print("*****************************************************************************************")
    print("          Your time is limited, so don't waste it living someone else's life.\n  Don't be trapped by dogma – which is living with the results of other people's thinking...")
    print("                                     -Steve Jobs-")
    print("*****************************************************************************************")
    print()
