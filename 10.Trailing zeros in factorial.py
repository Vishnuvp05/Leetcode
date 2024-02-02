# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Example 3:

# Input: n = 0
# Output: 0
# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Example 3:

# Input: n = 0
# Output: 

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        #the loop runs until the condition becomes false
        while(n!=0):
            a=n//5#dividing by five to find how many fives are there 
            count+=a # adding them to count
            n=a # assigning the fives to n to find how many fibes are inside this
        return count
    
# the no of zeros in the factorial is find by finding the no of zeros in the number lets us take examples
#in 5 --> 5*4*3*2*1=120 one zero because one five 
# let us see in 25 --> 25*24*23*... like we can see 2 fives and in 10 one five and in 20 one five and in 25 2 fives hence we have 6 fives
