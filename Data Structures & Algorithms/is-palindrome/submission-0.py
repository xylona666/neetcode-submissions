class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 反向积累字符串, 最后比较
        pos_res = []
        rev_res = []
        n =len(s)
        for i in s :
            if i.isalnum():
                pos_res.append(i.lower())
        new_pos_res = "".join(pos_res)
        for i in range(n-1,-1,-1):
            if s[i].isalnum():
                rev_res.append(s[i].lower())
        new_rev_res = "".join(rev_res)
        if  new_pos_res == new_rev_res:
            return True
        else:
            return False
