class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            s1 =heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            left = abs(s1-s2)
            heapq.heappush(stones,-left)
        return -stones[0] if stones else 0