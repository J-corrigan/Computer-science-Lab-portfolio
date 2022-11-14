import sys

def shift(rot):
    if rot in range(97, 110):
        rot = rot + 13
        return chr(rot)
    else:
        if rot == 32:
            return " "
        else:
            rot = rot - 13
            return chr(rot)

def rotter():
    word = []
    sub = (sys.argv[1:])
    sub = ' '.join(sub)
    sub = sub.lower()
    a = list(sub)
    for i in a:
        word.append(shift(ord(i)))
    print(str(''.join(word)))

rotter()
