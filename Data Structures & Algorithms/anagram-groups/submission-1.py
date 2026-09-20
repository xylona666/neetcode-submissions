class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # idea: act: "act","cat"
        dic  = defaultdict()
        res = []
        for i in strs:
            if "".join(sorted(i)) not in dic:
                dic["".join(sorted(i))] = [i]
            else:
                dic["".join(sorted(i))].append(i)
        for i in dic:
            res.append(dic[i])
        return res
