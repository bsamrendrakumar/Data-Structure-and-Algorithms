n=int(input("Enter a Number :-"))
sum=0
for i in range(1,n+1,1):
    if i%2 !=0:
        sum=sum+i
        print(sum,end=" ") 