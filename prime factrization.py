def solution(arr, num):
    primes = []
    if len(arr) == 0:
        return -1
    for i in range(2,num+1):
        while num%i == 0:
            primes.append(i)
            num = num//i
    if num > 2:
        primes.append(num)
    ans= 0
    for i in primes:
        if i < len(arr):
            ans += arr[i]
        else:
            return 0
    return ans

arr = [11,21,32,45,1,23]
num = 6

ans = solution(arr, num)
print("Answer is:",ans)