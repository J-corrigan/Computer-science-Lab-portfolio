import math as m

# TASK 1
name = input("what is your name?: ")
print("hello,", name, "Good to meet you!")

# TASK 2
celsius = input("Enter a temperature in Celsius: ")
celsius = float(celsius)
fahrenheit = (celsius*1.8) + 32
print(celsius,"C is equivalent to", fahrenheit,"F")

# TASK 3
students = input("How many students?: ")
students = int(students)
size = input("required group size?: ")
size = int(size)
print("There will be", m.ceil(students // size), "groups and", students % size, "students left over")

# TASK 4
students = input("how many students attended today?: ")
students = int(students)
sweets = input("how many sweets in the tub? ")
sweets = int(sweets)
print("each student will get:", m.ceil(sweets // students), "there will be", sweets % students, "left over.")