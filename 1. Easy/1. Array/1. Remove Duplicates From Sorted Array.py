#1. Using .pop() Time: O(n) [Traversing array once], Space: O(n) [.pop() will make copies of the array]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            
        #Edge cases (not required since we are returning len(nums))
        
        first = 0
        second = 1
        
        while second < len(nums): #prevent index out of range
            if nums[first] == nums[second]:
                nums.pop(first)
            else:
                first += 1
                second += 1
                
        return len(nums)
      
#2. Using two pointer apprach [One for insert index (everything before unique elements), one for i] Time: O(n) [Traversing array once], Space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #Edge case
        if not nums: return 0
        
        insertIndex = 1 #every element before insertIndex is unique
        
        for i in range(1, len(nums)): #starting from 1
            
            #If adjacent elements are different
            if nums[i] != nums[i - 1]:
                
                nums[insertIndex] = nums[i] #Copy value at i to insertIndex
                insertIndex += 1
                
        return insertIndex #return number of unique elements since 0-based index
      
 
