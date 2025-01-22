'''def climbingstais(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print(climbingstais(2))'''

'''def c(n):
    if n==0 or n==1:
        return 1
    return c(n-1)+c(n-2)
print(c(6))'''


'''def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        dp=[0]*len(cost)
        dp[0]=cost[0]
        if len(cost)>=2:
            dp[1]=cost[1]
        for i in range(2,len(cost)):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])'''

