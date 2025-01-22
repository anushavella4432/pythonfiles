#taking string as input

name=input("please enter your name:")
print('hello!',name,'Welcome to u')


#continution

age=input('enter your age:')
ages=int(age)
if ages<18:
    print('you are not ok')
elif ages==18:
    print('you are ok')
else:
    print('you are more ok')

#concatenation of strings

name=input('enter your name:')
age=input('enter your age:')
print('hello '+name+ ' your age is: '+ age)