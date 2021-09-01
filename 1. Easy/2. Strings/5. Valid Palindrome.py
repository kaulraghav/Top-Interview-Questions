#1. Get rid of anything apart from alphanum and convert into lowercase
#2. Reverse the formatted string and check if both are equal
#Time: O(n), Space: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        
        #1. removing extra characters and converting to lowercase
        for i in range(len(s)):
            if s[i].isalnum():
                new_s += s[i].lower()
                
        #2. reversing string and checking if they're equal, [[Creating list since strings are not mutable]]
        rev_s = list(new_s) 
        
        n = len(rev_s) - 1 #right side index to swap with 
        
        #if length is even
        if len(rev_s) % 2 == 0:
            for i in range(len(rev_s) // 2):
                rev_s[i], rev_s[n - i] = rev_s[n - i], rev_s[i]
                
        else: #odd length
            for i in range((len(rev_s) + 1) // 2):
                rev_s[i], rev_s[n - i] = rev_s[n - i], rev_s[i]
        
        return ''.join(rev_s) == new_s #join rev_s list
