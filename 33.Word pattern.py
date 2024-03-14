# 290. Word Pattern
# Easy
# Topics
# Companies
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=s.split()
        p_s={}
        s_p={}
        for p1,s1 in zip(pattern,a):
            if ((len(pattern)!=len(a))or(p1 in p_s and p_s[p1]!=s1) or (s1 in s_p and s_p[s1]!=p1)):
                return False
            p_s[p1]=s1
            s_p[s1]=p1
        return True


