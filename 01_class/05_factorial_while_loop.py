n = int(input("Enter a Number:-"))
factorial=1
i=1
if n<0:
    print("not exist")
elif n==0:
        print("0")
else:
     while i<=n:
           factorial=factorial*i
           i=i+1
           print("factorial of",i, "is ",factorial)