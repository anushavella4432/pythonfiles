def isprime(num):
    if num in (0,1):
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
num=int(input())
nextNum=num+1
while True:
    if isprime(nextNum):
        print(nextNum)
        break
    nextNum+=1

