class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in strings:
                strings[key] = []
            strings[key].append(s)

        return list(strings.values())