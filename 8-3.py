###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# read temperature in Celsius
celsius = float(input('Enter temperature in Celsius: '))

# convert Celsius to Kelvin and Fahrenheit
kelvin = celsius + 273.15
fahrenheit = (celsius * 9 / 5) + 32

# print results
print(f'Kelvin: {kelvin}')
print(f'Fahrenheit: {fahrenheit}')
