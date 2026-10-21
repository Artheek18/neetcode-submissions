class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        elements = []

        for num in nums:
            if num in freq:
                freq[num]+= 1
            else:
                freq[num] = 1
        
        elements = sorted(freq, key=freq.get, reverse=True)
        return elements[:k]
