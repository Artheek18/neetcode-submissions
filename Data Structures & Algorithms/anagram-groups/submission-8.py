class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for s in strs:
            counter = [0] * 26

            for char in s: 
                counter[ord(char) - ord("a")] += 1
            
            key = tuple(counter)

            if key not in groups:
                groups[key] = []
            
            
            groups[key].append(s)
        

        return list(groups.values())