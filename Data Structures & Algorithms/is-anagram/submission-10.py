class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        count = 1

        for string in s:
            if string in s_count:
                s_count[string] += 1
            else:
                s_count[string] = count
        
        for string in t:
            if string in t_count:
                t_count[string] += 1
            else:
                t_count[string] = count
        
        return s_count == t_count