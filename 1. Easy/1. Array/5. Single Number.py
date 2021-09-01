#1. Using a dict Time: O(n), Space: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dict = {}
        
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 0
            dict[nums[i]] += 1
            
        for k,v in dict.items():
            if v == 1:
                return k
              
#2. Using XOR operation Time: O(n), Space: O(1)

# - If we take XOR of zero and some bit, it will return that bit
#     - *a* ⊕ 0 = *a*
# - If we take XOR of two same bits, it will return 0
#     - a ⊕ a = 0
# - Single Number logic: *a* ⊕ *b* ⊕ *a*=( *a* ⊕ *a* )⊕ *b* = 0 ⊕ *b* = *b*

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
  
        mask = 0

        for i in range(len(nums)):
            mask ^= nums[i]
            
        return mask
