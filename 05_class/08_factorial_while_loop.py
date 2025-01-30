#factorial of n numbers
def sum_of(n):
    factorial=1
    i=1
    while i<=n:
        factorial=factorial*i
        i=i+1
        print(factorial)
sum_of(5)