class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        # The segment tree will have a size of 2 * n - 1, where n is the size of the input array
        self.tree = [0] * (2 ** math.ceil(math.log2(self.size)) * 2 - 1)
        self.build(0, 0, self.size - 1)

    def build(self, node, start, end):
        if start == end:
            # Leaf node, store the value from the original array
            self.tree[node] = self.arr[start]
        else:
            mid = start + (end - start) // 2
            # Recursively build the left and right subtrees
            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)
            # Combine the values of the left and right subtrees
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, idx, value):
        self._update(0, 0, self.size - 1, idx, value)

    def _update(self, node, start, end, idx, value):
        if start == end:
            # Leaf node, update the value in the original array and the tree
            self.arr[idx] = value
            self.tree[node] = value
        else:
            mid = start + (end - start) // 2
            if start <= idx <= mid:
                # Update in the left subtree
                self._update(2 * node + 1, start, mid, idx, value)
            else:
                # Update in the right subtree
                self._update(2 * node + 2, mid + 1, end, idx, value)
            # Update the value in the current node
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, left, right):
        return self._query(0, 0, self.size - 1, left, right)

    def _query(self, node, start, end, left, right):
        if left > end or right < start:
            # The query range is completely outside the current range
            return 0
        elif left <= start and right >= end:
            # The query range completely overlaps the current range
            return self.tree[node]
        else:
            mid = start + (end - start) // 2
            # Recursively query the left and right subtrees
            left_sum = self._query(2 * node + 1, start, mid, left, right)
            right_sum = self._query(2 * node + 2, mid + 1, end, left, right)
            return left_sum + right_sum


# Example usage:
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

print(seg_tree.query(1, 4))  # Output: 24 (sum of values in range [1, 4])

seg_tree.update(2, 9)
print(seg_tree.query(1, 4))  # Output: 28 (sum of updated values in range [1, 4])
