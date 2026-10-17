class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxheap
        # heapify and get hurt and pop k times
        #思路正确
        nnums = [-x for x in nums]
        heapq.heapify(nnums)
        for i in range(k):
            result = heapq.heappop(nnums)
        return -result