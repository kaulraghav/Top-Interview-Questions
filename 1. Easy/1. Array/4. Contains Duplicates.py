#Set logic, Time: O(n), Space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        
        for i in range(len(nums)):
            if nums[i] in unique:
                return True
            else:
                unique.add(nums[i])
            
        return False
