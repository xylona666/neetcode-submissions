class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 考虑直接sort,lambda key
        sn= sorted(s)
        tn = sorted(t)
 
        return sn == tn