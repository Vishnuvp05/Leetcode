# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # for i in ransomNote :
        #     if i not in magazine :
        #         return False 
        #     magazine = magazine.replace(i,'',1)
        # return True 
        c={}
        for i in magazine:
            if i not in c:
                c[i]=1
            else:
                c[i]+=1
        for i in ransomNote:
            if i in c and c[i]>0:
                c[i]-=1
            else:
                return False
        return True


        
        
        


        