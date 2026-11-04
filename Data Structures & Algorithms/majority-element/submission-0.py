class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        greatest = 0
        k = 0

        for num in nums:
            if num in majority:
                majority[num] += 1
            else: 
                majority[num] = 1
        
        for keys, values in majority.items():
            if  values > greatest:
                greatest = values
                k = keys
        
        return k