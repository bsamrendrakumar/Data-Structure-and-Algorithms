n=int(input("Enter a Number :-"))
odd=0
for i in range(1,n+1,1):
    if i%2 !=0:
        odd=odd+i
        print(odd,end=" ")