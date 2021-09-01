#123 => 1*100+2*20+3*1 should become 321 3*100+2*20+3*1*1, Building reverse while consuming original 
#Time: O()

class Solution:
    def reverse(self, x: int) -> int:
        
        #Edge cases
        if x < -2**31 or x > 2**31 - 1:
            return 0
        
        neg = False
        
        if x < 0: #if negative number 
            x *= -1
            neg = True

        zeroes = len(list(str(x))) 

        newX = 0
        
        while x > 0:

            rem = x % 10
            newX += rem * (10 ** (zeroes - 1))
            x = x // 10
            
            zeroes -= 1
        
        if neg: #change back to negative number
            return -1 * newX
        return newX
