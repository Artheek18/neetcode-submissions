class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for num in nums:
            if num in check:
                return True
            check[num] = num
        
        return False