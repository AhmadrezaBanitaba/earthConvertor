import math

# semi-major axis of earth
a = 6378137.0

# 1/f is reciprocal of flatteing 
f= 0.00335281068

# converts the input from degree to radians
latitude = math.radians(float(input('Enter Latitude:')))
longitude = math.radians(float(input('Enter Longitude:')))
height  = float(input('Enter Height:'))

def earthConverter(latitude, longitude, height):
	e = math.sqrt((2 * f) - (f**2))
	N = a / math.sqrt(1-e**2 * math.sin(latitude)**2)

	x = (N + height) * math.cos(latitude) * math.cos(longitude)
	y = (N + height) * math.cos(latitude) * math.sin(longitude)
	z = (N * (1 - e**2 ) + height) * math.sin(latitude)


	return x, y, z


# all values in meters
x,y,z = earthConverter(latitude, longitude, height)
print('x is %f' % x, 'm')
print('y is %f' % y, 'm')
print('z is %f' % z, 'm')











