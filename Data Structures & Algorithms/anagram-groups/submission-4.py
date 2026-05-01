class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            string = tuple(sorted(s))
            if string not in res:
                res[string] = []
            
            res[string].append(s)

        return res.values()
