'''n=100
a=(n*(n+1))//2 #sum of natural numbers
b=a+1
print(b%1000000007)'''

#18 sept 2023
'''n=3
a=(n*(n+1))/2
b=a+1
print(b%1000000007)'''
#performing some operations
'''n=int(input())
num=n
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        n //= 10  # Remove the last digit
        count += 1
if count>1:
    if num%2!=0:
        print(num//2)
    else:
        print((num-2)//2)
else:
    print(num)'''