#A subarray is a contiguous part of array.
#
# * Assume 1 based indexing.
#
# * The array contains both negative and positive values.
#
# * Assume the player is standing on a cartesian plane.
#
# Input Format
#
# - input1: An integer value N representing the number of shots made by the player
# - input2 : An integer K representing the size of subarray
# - input3 : An array of integers
#
# Sample Input
#
# N = 5
# K = 2
# distance values: 1 2 3 4 5
# index values:    1 2 3 4 5
# Sample output=32
#you task is to find and return an integer value representing the max possible score you can achive by choosing
#a contingous sub array of size k from array
n=5
k=3
arr=[9,2,1,3,7]
ans=0
for i in range(0,n-k+1):
    sub_arr=arr[i:i+k]
    print("find the score for sum sub arr",sub_arr)
    sum=0
    for j in range(1,k+1):
        sum+=sub_arr[j-1]*j
        print("the sum is",sum)
    print("score is",sum)
    if sum>ans:
        ans=sum
print(sum)