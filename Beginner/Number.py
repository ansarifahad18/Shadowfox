# -----------------------------------------
# Question 1: format() with 145 and 'o'
# -----------------------------------------
result = format(145, 'o')
print("Octal representation of 145:", result)


# -----------------------------------------
# Question 2: Area of circular pond + water calculation
# -----------------------------------------
pi = 3.14
r = 84

area = pi * (r ** 2)
print("Area of the pond:", area)

water = area * 1.4
print("Water in pond (liters):", int(water))  


# -----------------------------------------
# Question 3: Speed calculation
# -----------------------------------------
distance = 490
time_seconds = 7 * 60  # convert minutes to seconds

speed = distance / time_seconds
print("Speed in m/s:", int(speed)) 
