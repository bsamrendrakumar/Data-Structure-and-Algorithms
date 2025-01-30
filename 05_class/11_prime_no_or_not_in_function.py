def number(n):
    i=2
    while i<=n+1:
        if n%i==0:
            print("Non Prime")
            break
        else:
            i=i+1
            print("Prime")
            break
number(5)