#Dictionary + .index() function
#Time: O(n), Space: O(1)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dict = {}
        
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 0
            dict[s[i]] += 1
            
        for k, v in dict.items():
            if v == 1:
                return s.index(k) #.index() returns the first index of the matching value
            
        return -1
