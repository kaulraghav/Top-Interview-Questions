#Time: O(n), Space: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        
        while n > 0: #All digits become 0 after right shifting
            if n & 1 == 1:
                count += 1
            n = n >> 1 #Right shift
        
        return count
