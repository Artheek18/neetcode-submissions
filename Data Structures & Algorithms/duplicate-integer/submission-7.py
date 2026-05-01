class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        find_duplicates = {}
        for num in nums:
            if num in find_duplicates:
                return True
            else:
                find_duplicates[num] = num

        return False
