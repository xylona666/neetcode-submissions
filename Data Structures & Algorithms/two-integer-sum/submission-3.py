class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = defaultdict(int)
        for i in range(len(nums)):
            hm[nums[i]] = i
        for i in range(len(nums)):
            left = target-nums[i]
            if left in hm:
                second = hm[left]
                if i != second:
                    return [i,second]


       