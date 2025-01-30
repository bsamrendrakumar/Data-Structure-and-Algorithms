#calculate sum of 1 to n
def sum_of(n):
    sum=0
    for i in range(1,n+1,1):
        sum=sum+i
        print(sum)
sum_of(5)