#Basic Dictionary Solution
#Time: O(n), Space: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = {}
        t_dict = {}
        
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 0
            s_dict[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in t_dict:
                t_dict[t[j]] = 0
            t_dict[t[j]] += 1
            
        return s_dict == t_dict
