class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_prod = nums[0]
        Min, Max = 1, 1
        


        for i in range(len(nums)):
            temp = Max * nums[i]
            Max = max(nums[i] * Max, nums[i] * Min, nums[i])
            Min = min(temp, nums[i] * Min, nums[i])
            max_prod = max(max_prod, Max)
            print(max_prod)

        return max_prod