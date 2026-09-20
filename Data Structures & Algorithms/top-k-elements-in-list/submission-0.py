class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int) # defaultdict和dic.get(num,0)的区别
        for i in nums:
            dic[i] +=1
        sorted_dict= sorted(dic.items(),key = lambda x:x[1],reverse = True)
        result = []
        for i in range(k):
            result.append(sorted_dict[i][0])
        return result

        