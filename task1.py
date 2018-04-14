from math import pi

def calculate (R, L):
	volume = pi * R * R * L
	return ('Volume of cylinder is: ' + str(volume))
R = int(input('Please Enter the Radius of Cylinder: '))
L = int(input('Please Enter the Height of Celinder: '))
print ("pi=")
print (pi)
print (calculate(R, L))
