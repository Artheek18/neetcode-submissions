class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        k = 0
        triples = []
        nums.sort()   

        for k in range(len(nums)):
            if nums[k] > 0:
                break

            elif k > 0 and nums[k] == nums[k-1]:
                continue

            start = nums[k] 
            i, j = k + 1, len(nums)-1
            while i < j:
                if start + nums[i] + nums[j] < 0:
                    i += 1
                
                elif start + nums[i] + nums[j] > 0:
                    j -= 1

                elif start + nums[i] + nums[j] == 0:
                    triples.append([start, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                    
        return triples