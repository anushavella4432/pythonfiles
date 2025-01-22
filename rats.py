'''r=7
unit=2
n=8
arr=[2,8,3,5,7,4,1,2]
d=r*unit
f=0
if not arr:
    print('-1')
for i in range(n):
    f+=arr[i]
    if f>=d:
        print(i+1)
        break
else:
    print('0')'''

s = input()
for i in range(0,len(s)):
    count = 0
    for j in s:
        if int(j)==i:
            count+=1
        else:
            pass
    if count != int(s[i]):
        print("It is not a autobiographical number")
        print('0')
        break
else:
    l=[]
    for i in s:
        if int(i)!=0:
            l.append(i)
    print(len(l))
    print("It is a autobiographical number")