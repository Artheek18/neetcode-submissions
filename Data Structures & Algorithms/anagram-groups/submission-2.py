class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_index = {}
        for string in strs:
            s = tuple(sorted(string))
            if s not in str_index:
                str_index[s] = []
            str_index[s].append(string)

        return list(str_index.values())


        