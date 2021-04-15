def proMax(arr):
    dp = [a for a in arr]
    for i in range(0,len(arr)):
        for j in range(0,i):
            if arr[i]%arr[j] == 0:
                dp[i] = max(dp[i],dp[j]+arr[i])
    return max(dp)
n=int(input())
arr = [int(i) for i in input().split()]
print(proMax(arr))
