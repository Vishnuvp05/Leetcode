#Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

class Solution: #But the time limit exceeds here
    def majorityElement(self, nums: List[int]) -> int:
        a=len(nums)/2
        for i in nums:
            if nums.count(i)>a:
                return i
            
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(set(nums), key=nums.count)
        
            
            