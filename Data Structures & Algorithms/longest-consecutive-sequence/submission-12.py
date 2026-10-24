class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seq = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                counter = 1
                while (num + counter) in nums_set:
                    counter +=1
                seq = max(seq, counter)
    
        return seq
    
                    


