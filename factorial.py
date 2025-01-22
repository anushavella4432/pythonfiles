#factorial without recursion

num=int(input('enter a number'))
factorial=1
if num<0:
    print('factorial does not exist')
elif num==0:
    print('factorial of 0 is 1')
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print('the factorial of',num, 'is',factorial)


#FACTORIAL with recursion

def factorial(x):
    if x==1:
        return 1
    else:
        return(x*(factorial(x-1)))
x=int(input('enter a number'))
result=factorial(x)
print(result)