class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s)) + '#' + s for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find where the length ends (at '#')
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])      # parse length
            word = s[j+1:j+1+length] # grab substring of that length
            res.append(word)
            i = j + 1 + length       # move to next encoded string
        return res
                 