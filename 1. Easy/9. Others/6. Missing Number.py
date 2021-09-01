#Cyclic sort (equating elements with their index), 2-pass
#Time: O(n), Space: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #first pass (sorting numbers to their correct index) [[Use while loop instead of for, because we only increment our index when we know the element is sorted for that index]]
        i = 0
    
        while i < len(nums):
            j = nums[i]
            
            if i != j and j < len(nums): #ele not at correct place and can be swapped
                nums[i], nums[j] = nums[j], nums[i]
                
            else: #Important
                i += 1
        
        print("Sorted list:", nums)
        
        #second pass (comparing which element is out of place)
        for i in range(len(nums)):
            j = nums[i]
            
            if i != j:
                return i
        
        return len(nums)
