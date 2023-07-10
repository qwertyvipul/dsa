def maxSubArraySum(nums):
    globalMax = float("-inf")
    localMax = 0
    
    for num in nums:
        localMax = localMax + num
        
        globalMax = max(globalMax, localMax)
        
        if localMax < 0:
            localMax = 0
            
    return globalMax

nums = [-2, -3, 4, -1, -2, 1, 5, -3]

print(maxSubArraySum(nums)) # 7