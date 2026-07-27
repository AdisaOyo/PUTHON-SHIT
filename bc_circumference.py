import math

print (' "CODE TO CALCULATE THE CIRCUMFERENCE OF A CIRCLE" ')

r = float (
    input ("What is the radius? ")
)
circ = math.ceil(
    2*math.pi*r
    )
area = round(
    math.pi * pow(r, 2), 2
    )

print(
    f"The area is {area}"
    )
print(
    f"The circumference is {circ}"
    )