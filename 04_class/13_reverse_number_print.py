n = int(input("Enter a Number :- "))
a=0
for i in range(n):
    a=a+i
var = a+n
for r in range(n):
    for c in range(r+1):
        print(var,end=" ")
        var=var-1
    print() 