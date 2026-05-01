class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        maxLength, currentLength = 1,1
        sequence = sorted(set(nums))
        for i in range(1, len(sequence)):
            if sequence[i] - sequence[i-1] == 1:
                currentLength +=1

            elif sequence[i] - sequence[i-1] != 1:
                maxLength = max(maxLength, currentLength)
                currentLength = 1
        
        maxLength = max(maxLength, currentLength)

        return maxLength 