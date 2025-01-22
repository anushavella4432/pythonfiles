
def superior(arr, n):
    count=0
    sup=-float('inf')
    for i in range(n-1,-1,-1):
        if arr[i]>sup:
            count+=1
            sup=arr[i]
    return count
n = int(input())
arr = list(map(int, input().split()))
print(superior(arr, n))