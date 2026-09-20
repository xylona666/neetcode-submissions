

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        # 1. 统计频率
        for num in nums:
            freq[num] += 1

        heap = []

        # 2. heap 中保存 (频率, 数字)
        for num, count in freq.items():

            heapq.heappush(heap, (count, num))

            # 只保留 k 个
            if len(heap) > k:
                heapq.heappop(heap)

        # 3. heap 中剩下的就是 Top K
        result = []

        while heap:
            count, num = heapq.heappop(heap)
            result.append(num)

        return result