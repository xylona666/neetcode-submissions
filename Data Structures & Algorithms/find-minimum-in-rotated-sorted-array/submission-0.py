class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find min
        left = 0
        right = len(nums)-1
        minimin = nums[0]
        while left<=right:
            mid = (left+right)//2
            if nums[mid]<nums[right]:
                minimin =min(minimin,nums[mid])
                right = mid-1
            else:
                minimin =min(minimin,nums[left])
                left = mid+1
        return minimin