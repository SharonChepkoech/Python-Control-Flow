# Using the range function, for loop and if, elif, else statements. 
# Create a program that prints all the numbers that are divisible by 5, 6, 7,  9, or all
a = range(100)
for b in a:
    if b %5 == 0 and b %6 == 0 and b %7  == 0 and b %9 ==0:
            print(f"{b} is divisble by all")
    elif b %5 == 0 and b %7 == 0:
            print(f"{b}divisble by 5 and 7")
    elif b %5 == 0 and b %6 == 0:
        print(f"{b}divisble by 5 and 6 ")
    elif b %5 == 0 and b %7 == 0:
        print(f"{b}divisble by 5 and 7")
    elif b %5 == 0 and b %9 == 0:
        print(f"{b}divisble by 5 and 9")
    elif b %6 == 0 and b %7 == 0:
        print(f"{b}divisble by 6 and 7")
    elif b %6 == 0 and b %9 == 0:
        print(f"{b}divisble by 6 and 9")
    elif b %7 == 0 and b %9 == 0:
        print(f"{b}divisble by 7 and 9")