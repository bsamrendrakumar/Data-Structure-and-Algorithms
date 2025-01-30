def sum_of_dig(num):
    dig_sum = 0
    while num>0:
        last_dig = num%10
        num = num/10
        dig_sum = dig_sum + last_dig
        print(dig_sum)
sum_of_dig(145)      
