#TASK 5

import sys

def temps(*lst):
    cont = True
    valis = []
    lst = sys.argv
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