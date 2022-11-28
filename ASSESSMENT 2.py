print("""
Park Run Timer
~~~~~~~~~~~~~~
""")

runners = []
times = []

def runner(number, time):
    return f"> {number}::{time}"

def average(time):
    return "average"

def fastest(time):
    return "fastest"

def slowest(time):
    return "slowest"

def main():
    d = 0
    e = "Error in data stream. Ignoring. Carry on.!"
    check = True
    while check:
        init = input("> ")
        if init == "::":
            print(e)
            continue
        data = init.split("::")
        if "" in data:
            print (e)
            continue
        if init == "END":
            c = min(runners)
            print(f"total runners: {d}")
            print(average(times))
            print(fastest(times))
            print(slowest(times))
            print(f"Best time here: Runner #{c[1]}")
            break

        try:
            a = (data[0])
            b = (data[1])
            runners.append([b, a])
            times.append([b])
            d = d + 1
            continue

        except:
            print(e)
            continue

main()
