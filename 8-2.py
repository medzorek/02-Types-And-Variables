###
# Calculation of circle area and circumference
#

# determine radius and PI values
r = float(input('Enter radius: '))
pi = 3.14

# calculate area
area = pi * r * r

# calculate circumference
circumference = 2 * pi * r

# print results
print(f'Circumference: {circumference:.2f}')
print(f'Area: {area:.2f}')
