"""
CODE TO CALCULATE THE AREA OF A TRIANGLE
"""
print (' """CODE TO CALCULATE THE AREA OF A TRIANGLE""" ')
base = float( input("What is the triangle's base? "))
height = float( input("What is the triangle's height? "))

area = 1.5 * base * height
area = round(area,3)
print (f"The area of the triangle is: {area:,.3f}")
