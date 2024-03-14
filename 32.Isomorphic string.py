# 205. Isomorphic Strings
# Easy
# Topics
# Companies
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t={}
        t_s={}        
        for s1,t1 in zip(s,t):
            if ((s1 in s_t and s_t[s1]!=t1) or (t1 in t_s and t_s[t1]!=s1)):
                return False
            s_t[s1]=t1
            t_s[t1]=s1
        return True    
        