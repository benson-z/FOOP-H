import math

angle = math.radians(float(input("What is the angle(degrees)?\n")))
print("The angles of the triangle are {a}, {b}, and {c}".format(a=angle, b=90.0, c=90-angle))
print("The ratio of the triangle sides are {a}, {b}, and {c}".format(a=abs(math.sin(angle)), b=abs(math.cos(angle)), c=1.0))