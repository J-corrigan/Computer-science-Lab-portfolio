# TASK 1
name = input("what is your name?: ")
if name == "":
    print("Hello Stranger!")
else:
    print("hello,", name, "Good to meet you!")

# TASK 2, 3, 4, 5.
set = False
restart = False
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while set == False:
        password = input("please enter a new password: ")
        Pconf = input("please confirm: ")
        if (len(password) < 8 or len(password) > 12) or (password in BAD_PASSWORDS):
            print ("ERROR")
            answer = str(input("run again? y/n: "))
            if answer == "y":
                continue
            else:
                print ("goodbye")
                break
        if password == Pconf:
            print("password set!")
            set = True
        elif password != Pconf:
            print("ERROR! password confirmation did not match!")

# TASK 6, 7, 8.
a = input("enter a number: ")
a = int(a)
for i in range(0, a+1):
    print(i, 'x', 7, "=", i * 7)
if a < 0:
    a = -(a)
    for i in range(a, 0 , -1):
        print(i, 'x', 7, "=", i * 7)

