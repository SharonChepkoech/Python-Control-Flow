a = range(100)
for b in a:
    if b % 5 == 0 and b % 6 == 0 and b % 7 == 0 and b %9 == 0:
        print(f"{b} is divisble by all")
    elif b % 5 == 0:
        print(f"{b} is divisble by 5")
    elif b % 6 == 0:
        print(f"{b} is divisble by 6")
    elif b % 7 == 0:
        print(f"{b} is divisble by 7")
    elif b % 9 == 0:
        print(f"{b} is divisble by 9")  