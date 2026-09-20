class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict() # key:num
        res =[]
        for i in range(len(nums)):
            nex = target-nums[i]
            if nex in dic:
                res.append(dic[nex])
                res.append(i)

            else:
                dic[nums[i]] = i
        return res
