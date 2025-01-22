a=int(input())
b=list(map(int,input().split()))
count=0
s=0
for i in (b):#for i in range(a):
    s+=i    #s+=a[i]
    if s==0:
        count+=1
print(count)