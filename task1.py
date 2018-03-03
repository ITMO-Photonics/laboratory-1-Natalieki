import math
pi = 3.14
def calculate (R, L):
	volume = pi * R * R * L

	return ('Volume: ' + str(volume))



R = int(input('Please Enter the Radius of Cylinder: '))
L = int(input('Please Enter the Height of Celinder: '))

print (calculate(R, L))

