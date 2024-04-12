import random
from collections import defaultdict      

n = 10
nums = [random.randint(1, n) for i in range(n)]

# Brute force
res = 0
for i in range(n):
    for j in range(i, n):        
        res += sum(set(nums[i:j+1]))


# Count contribution
occurences = defaultdict(list)
for i, num in enumerate(nums):
    occurences[num].append(i)

res2 = 0
for num in occurences:
    occurences[num].append(n)
    for i in range(len(occurences[num])-1):
        cur = occurences[num][i]
        nxt = occurences[num][i+1]
        res2 += (nxt - cur) * num
        res2 += cur * (nxt - cur) * num
        print((nxt - cur) * (1 + cur) * num)
       
# Count contribution one liner
d = occurences
res3 = sum(sum((nxt - cur) * (1 + cur) * num for cur, nxt in zip(d[num][:], d[num][1:])) for num in d)
        
print(res == res2 == res3)