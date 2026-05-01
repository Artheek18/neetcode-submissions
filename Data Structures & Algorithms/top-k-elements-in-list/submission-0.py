class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        k_map = []

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
                
        for i in range(k):
            max_key = 0
            max_freq = -1
            for key, freq in freq_map.items():
                if freq > max_freq:
                    max_key = key
                    max_freq = freq
            k_map.append(max_key)
            del freq_map[max_key]  # Remove the element with max frequency from the dictionary
        
        return k_map
        

        
            

