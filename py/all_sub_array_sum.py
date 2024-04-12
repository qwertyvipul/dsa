import random
from itertools import accumulate

n = 10
nums = []
for i in range(n):
    nums.append(random.randint(1, n))
    
p = [0] + list(accumulate(nums))

# Brute force
res = 0
for i in range(n):
    for j in range(i, n):
        res += p[j+1] - p[i]

# Count contribution
res2 = 0;
for i, num in enumerate(nums):
    res2 += (n - i) * num
    res2 += i * (n - i) * num

# One liner brute force
res3 = sum(sum([p[j+1] - p[i] for j in range(i, n)]) for i in range(n))

# One liner count contribution
res4 = sum((i + 1) * (n - i) * num for i, num in enumerate(nums))

print(res == res2 == res3 == res4)