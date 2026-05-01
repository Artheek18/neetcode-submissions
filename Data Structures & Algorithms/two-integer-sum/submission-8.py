class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}
        
        for i in range(len(nums)):
            num = nums[i]
            difference = target - num
            if difference in two_sum:
                return [two_sum[difference], i]
            
            two_sum[num] = i
        

        return []
            