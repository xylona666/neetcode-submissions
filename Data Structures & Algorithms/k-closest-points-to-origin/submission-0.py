class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        result = []
        for point in points:
            lst.append((point[0]**2+point[1]**2,point))
        heapq.heapify(lst)
        while len(result)<k:
            value, point = heapq.heappop(lst)
            result.append(point)
        return result