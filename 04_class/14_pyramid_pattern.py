n=int(input("Enter a Number :- "))
for i in range(n):
    #space n-i-1
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()