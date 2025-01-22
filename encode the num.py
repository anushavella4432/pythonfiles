'''n=input()
res=""
for i in n:
    cur_num=int(i)
    res+=str(cur_num**2)
print(res)'''


n=int(input())
res=""
while n>0:
    cur_num=n%10
    res=str(cur_num**2)+res
    n=n//10
print(res)