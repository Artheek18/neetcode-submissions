class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_count = {}
        s_count = {}

        for c in s:
            if c in s_count:
                s_count[c] += 1
            else:
                s_count[c] = 1
        
        for a in t:
            if a in t_count:
                t_count[a] += 1
            else:
                t_count[a] = 1
        
        return s_count == t_count



        