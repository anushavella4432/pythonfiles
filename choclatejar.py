def choc(A,N):
    total_choc=0
    for i in N: 
        if i%3==0:
            j=i//3
            total_choc+=j
        else:
           j=i//3
           total_choc+=j
           total_choc+=1
    return total_choc
A=int(input())
N=list(map(int,input().split(" ")))
print(choc(A,N))

'''n=int(input())
arr=list(map(int,input().split(" ")))
totalchoc=0
for numberofchocs in arr:
    totalchoc+=(numberofchocs//3)
    if numberofchocs%3!=0:
        totalchoc+=1
print(totalchoc)'''