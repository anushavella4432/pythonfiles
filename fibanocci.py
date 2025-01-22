#without recursion
n=int(input('enter a num'))
num1=0
num2=1
next_number=num2
count=1
while count<=n:
    print(next_number,end='  ')
    count+=1
    num1,num2=num2,next_number
    next_number=num1+num2


    #with recursion
def fib(n):
    if n<0:
        print('incorrect input')
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
n=int(input('enter a number'))
print(fib(n))
