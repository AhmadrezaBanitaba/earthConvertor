import math
import csv


# semi-major axis of earth
a = 6378137.0

# 1/f is reciprocal of flatteing 
f= 0.00335281068



def earthConverter(latitude, longitude, height):
	e = math.sqrt((2 * f) - (f**2))
	N = a / math.sqrt(1-e**2 * math.sin(latitude)**2)

	x = (N + height) * math.cos(latitude) * math.cos(longitude)
	y = (N + height) * math.cos(latitude) * math.sin(longitude)
	z = (N * (1 - e**2 ) + height) * math.sin(latitude)


	return x, y, z



with open('worksheet.csv', 'r') as Infile, open('worksheet_out.csv', 'w') as Outfile:
    reader = csv.reader(Infile)
    writer = csv.writer(Outfile)
    for row in reader:
        lat = math.radians(float(row[0]))
        lon = math.radians(float(row[1]))
        ht = math.radians(float(row[2]))
        x, y, z = earthConverter(lat, lon, ht)
        row_out = [row[0], row[1], row[2], x, y, z]
        writer.writerow(row_out)








