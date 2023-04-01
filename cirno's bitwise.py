t = int(input())
for _ in range(t):
    x = int(input())

    if x == 1:
        print(3)

    # check it x is odd or even if it is odd then y will be 1 
    # if it's even y will be x + 1 if x is power of 2 or divide the even number x by 2 while
    # doubling y until u get odd number x
 
    else: 
        temp = x  
        y = 1
        while x:
            if x & 1:
                break
            y *= 2
            x //= 2

        if temp == y:
            y += 1

        print(y)
