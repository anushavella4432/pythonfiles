'''s=int(input())
a=list(map(int,input().split()))'''
s=10
a=[9,9,9,3,3,3,1,1,1,5]
counter={}
for i in a:
    if i in counter:
        counter[i]+=1
    else:
        counter[i]=1
#print(*counter.items())
'''ans=0
maxvalue=0
for key,value in counter.items():
    maxvalue=value
    ans=key
print(ans)'''

newarray=list(counter.items())
newarray.sort(key = lambda ele:ele[1])
#print(newarray)
if newarray[-1]>newarray[-2]:
    print(newarray[-1])
else:
    print(-1)