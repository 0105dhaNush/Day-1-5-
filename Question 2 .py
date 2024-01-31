n = 20
for i in range(1,n + 1):
    # print leading spaces
    for j in range(n - i):
        print("",end="")

    # print increasing numbers
    for k in range(1, i + 1):
        print(k,end="")

    # print decreasing numbers
    for I in range(i - 1,0,-1):
        print(i,end="")

    # move to next line after each row
    print()