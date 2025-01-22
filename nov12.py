'''arr=[12,3,14,56,77,13]
num=13
diff=2
count=0
for i in range(len(arr)):
    if abs(num-arr[i])<=diff:
        count+=1
print(count)'''

#equilibrium
'''arr=[3,4,3,1,6]
for i in range(len(arr)):
    left,right=sum(arr[:i]),sum(arr[i+1:])
    if left==right:
        print(i)
'''

