# TASK 1
def parameter(a):
    """if value is less out of range 0-100, returns false"""
    if 0 > a or a > 100:
        print(False) 
    else:
        print (True)

a = input("input a value: ")
a = int(a)
parameter (a)

# TASK 2
def upperlower (txt):
    """returns how many upper/lowercase letters are present in a word."""
    U = 0
    L = 0
    for i in txt:
        if str.isupper(i):
            U = U + 1       
        if str.islower(i):
            L = L + 1
    print ("there are", U, "uppercase letters.")
    print ("there are", L, "lowercase letters")

txt = input ("input a word: ")
upperlower (txt)

#TASK 3
name = input("WHat is your name?: ")
def modifier(name):
    """the modifier function here will rework string so that the first letter is capital, 
       and the remaining letters are lowercase."""
    if name == "":
        print("Hello Stranger!")
    else:
        modname = ((name[0]).upper() + (name[1:]).lower())
        print("hello,", modname, "Good to meet you!")

modifier(name)

#TASK 4
string = input("please input a new string: ")
if len(string) < 2:
    print(string)
else:
    remove = lambda: print(string.rstrip(string[-1]))
    remove()

#TASK 5
def convertc():
    celsius = input("please input a temperature in degrees celsius: ")
    celsius = int(celsius)
    fahrenheit = (celsius * 1.8) + 32
    print(fahrenheit, str("F"))
convertc()


def convertf():
    fahrenheit = input("please input a temperature in degrees celsius: ")
    fahrenheit = int(fahrenheit)
    celsius = (fahrenheit - 32) / 1.8
    celsius = round (celsius, 2)
    print(celsius, str("C"))
convertf()

#TASK 6
