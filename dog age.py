'''def dog_age(N):
    return (N*7)
N=int(input())
print(dog_age(N))'''

n=5
for i in range(1,n):
    for j in range(i,n-1):
        print('*',end='')
print()