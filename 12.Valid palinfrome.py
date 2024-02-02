# Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #It filters out the characters that are not alphanumeric using the isalnum() method of the str class
        #It joins the remaining characters into a new string using the join() method of the str class with an empty string as the separator
        a=("".join(letter for letter in s if letter.isalnum())).lower()
        b=a[::-1]#revese the filtered string 
        if a==b:#checks for palindrome
            return True 
        else:
            return False
