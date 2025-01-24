n=int(input("Enter a Number :-"))
even_sum=0
for i in range(1,n+1,1):
    if i%2 ==0:
        even_sum=even_sum+i
        print(even_sum,end=" ")