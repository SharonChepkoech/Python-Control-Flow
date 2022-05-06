x = range(20)
for y in x:
    if y % 2==0 & y %3 ==0:
        print(f"{y} is divisble by 2 and 3")
    elif y % 2==0:
        print(f"{y} is divisble by 2")
    elif y %3 == 0:
        print(f"{y} is divisble by 3" )
    else:
        print(f"{y} is not divisble by 2 or 3")        