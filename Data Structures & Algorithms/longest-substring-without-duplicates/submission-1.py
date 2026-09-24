class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_count = 0
        se = set()
        left= 0
        right = 0
         
        while right < len(s):
            if s[right] in se :
                se.remove(s[left])
                left+=1
            else:
                
                se.add(s[right])
                max_count = max(right-left+1,max_count)
                right +=1
        return max_count

                


