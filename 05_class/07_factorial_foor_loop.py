#factorial of n numbers
def sum_of(n):
    factorial=1
    for i in range(1,n+1,1):
        factorial=factorial*i
        print(factorial)
sum_of(5)