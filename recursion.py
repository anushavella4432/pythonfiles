#factorial using recursion

'''def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))'''



#write a recursive program to print a number in reverse order

'''def rev(n):
    if n==0:
        return n
    print(n%10)
    return(n//10)'''


    
#write a recursive function to count the no of digits of a number

'''def cod(n):
    if n==0:
        return 0
    else:
        return cod(n//10)+1
print(cod(12345))'''

    

#write a recursive function to calculate the sum of digits

'''def sod(n):
    if n==0:
        return 0
    else:
        r=n%10
        return r+sod(n//10)
print(sod(12345))'''


#armstrong number

'''def cod(n):
    if n<10:
        return 1
    else:
        return cod(n//10)+1
n=int(input(''))
count=cod(n)
print(count)
def arm(n):
    if n==0:
        return 0
    r=n%10
    return r**count+arm(n//10)
print(arm(n))'''