#Stack and Dictionary Solution
#Time: O(n), Space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        
        dict = {")" : "(", #Keep closing brackets as keys, since we search and access dict[values] for comparison  
                "}" : "{",
                "]" : "["}
        
        stack = []
        
        for i in s:
            if i in dict: #closing bracket
                ele = stack.pop() if stack else "#" #Takes care of cases '[,(,{'
                
                if ele != dict[i]:
                    return False
                
            else: #opening bracket
                stack.append(i)
                
        return False if stack else True #if any element is remaining, return False
