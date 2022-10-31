# TASK 1
def parameter(a):
    """if value is out of range 0-100, returns false"""
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
    fahrenheit = input("please input a temperature in degrees Fahrenheit: ")
    fahrenheit = int(fahrenheit)
    celsius = (fahrenheit - 32) * 0.5556
    print(celsius, str("F"))
convertf()

#TASK 6
def convertfe():
    ret = False
    while ret == False:
        inquire = ["c","C"]
        fahrenheit = input("please input a temperature in degrees celsius: ")
        exc = fahrenheit.split()
        if exc [-1] in inquire:
            exc = exc[0]
            exc = int(exc)
            fahrenheit = (exc * 1.8) + 32
            print (fahrenheit, " F")
            break
        else:
            print ("invalid syntax")
            continue

convertfe()

#TASK 7/8
def temps(*lst):
    cont = True
    valis = []
    lst = input("input values: ")
    lst = lst.split()
    for i in lst:
        if len(i) == 1:
            print("invalid syntax")
            cont = False
        else:
            val = i.strip('c')
            val = int(val)
            valis.append(val)

        if cont == False:
            break

    if cont == True:
        from statistics import mean
        print("the smallest value is ", min(valis))
        print("the largest value is ", max(valis))
        print("the mean is ", mean(valis))

temps()
