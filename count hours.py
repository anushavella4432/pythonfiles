#imp
'''def count_full_hours():
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n <= 1:
        print("NO HOURS")
        return
    
    mod = (10**9) + 7
    remainder_count = [0] * 60  # To store the frequency of remainders
    ans = 0
    
    for num in arr:
        remainder = num % 60
        complement = (60 - remainder) % 60
        ans = (ans + remainder_count[complement]) % mod
        remainder_count[remainder] += 1
    
    print(ans if ans > 0 else "NO HOURS")

count_full_hours()
'''
#maximum sum subarray printing
'''n = int(input())  # Input the number of elements in the array
arr = list(map(int, input().split()))  # Input the array

current_subarray = []  # To hold the current subarray
max_subarray = []  # To hold the maximum subarray
current_sum = 0  # The sum of the current subarray
max_sum = arr[0]  # Initialize with the first element of the array

for i in range(n):
    if current_sum + arr[i] < arr[i]:
        current_sum = arr[i]
        current_subarray = [arr[i]]  # Start a new subarray
    else:
        current_sum += arr[i]
        current_subarray.append(arr[i])  # Continue the current subarray

    if current_sum > max_sum:
        max_sum = current_sum
        max_subarray = current_subarray[:]  # Update the max subarray

# Print the maximum sum and the subarray
print("Maximum sum:", max_sum)
print("Subarray with maximum sum:", max_subarray)'''

