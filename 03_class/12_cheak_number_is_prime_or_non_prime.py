n=int(input("Enter a Number :-"))
for i in range(2,n-1,1):
    if n%i==0:
        print("Non Prime")
        break
    else:
        print("Prime")