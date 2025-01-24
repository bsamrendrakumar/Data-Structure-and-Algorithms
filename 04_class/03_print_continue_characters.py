n=int(input("Enter a Number :- "))
ch = "A"
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(ch,end=" ")
        ch=ch+1
    print(" ")