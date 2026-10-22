class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}??????{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find where the length ends
            while s[j] != "?":
                j += 1

            length = int(s[i:j])
            start = j + 6  
            result.append(s[start:start + length])
            i = start + length

        return result

