class BITree:
    def __init__(self, n):
        self.size = n
        self.nums = [0] * (n+1)
    
    def update(self, i, val):
        i += 1
        while i <= self.size:
            self.nums[i] += val
            i += i & -i
    
    def query(self, i):
        i += 1
        res = 0
        while i:
            res += self.nums[i]
            i -= i & -i
        return res
    
nums = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2]
biTree = BITree(len(nums))

for i, num in enumerate(nums):
    biTree.update(i, num)

from itertools import accumulate
p1 = list(accumulate(nums))

p2 = []
for i in range(len(nums)):
    p2.append(biTree.query(i))
    
print(p1 == p2)
            
        