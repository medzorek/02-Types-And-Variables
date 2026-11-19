###
# Distance to the horizon in km based on height in meters
#
import math

h = float(input("Enter height in meters: "))
d = 3.57 * math.sqrt(h)
print("Distance to the horizon (km):", d)
