class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i in range(len(nums)):
            num = nums[i]
            needed = target - num

            if needed in index:
                return [index[needed], i]
            
            index[num] = i

        return []
        
        