#Traverse till middle element, swap s[i] with s[n - i] Time: O(n/2 ==> n), Space: O(1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s.reverse()
        
        n = len(s) - 1
        
        #if even
        if len(s) % 2 == 0:
            print("Even")
            for i in range(len(s) // 2):
                s[i], s[n - i] = s[n - i], s[i]
               
        else: #if odd
            print("Odd")
            for i in range((len(s) + 1) // 2):
                s[i], s[n - i] = s[n - i], s[i]
