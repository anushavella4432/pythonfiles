'''def diwali(N,A):
    s=240-A
    r=0
    ps=0
    for i in range(1,N+1):
        r+=5*i
        if s>=r:
            ps+=1
        else:
            break
    return ps
N=int(input())
A=int(input())
print(diwali(N,A))'''


'''n=6
a=180
s=240-a
rc=0
count=0
for i in range(1,n+1):
    rc+=5*i
    if rc<=s:
        count+=1
    else:
        break
print(count)'''
 
n=int(input())
travel_time=int(input())
count=0
remaining_time=240-travel_time
for i in range(1,n+1):
    solve_time=i*5
    if solve_time<remaining_time and remaining_time>0:
        count+=1
        remaining_time-=solve_time
print(count)
        