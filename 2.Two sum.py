#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.
#creating solution using nested loops with a time complexity O(n^2) 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return ([i,j])  
                
#using hashfunction 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i,num in enumerate(nums):
            if target-num in seen:# Check if the complement of the current number, i.e. target - num, is already in the seen dictionary
                return ([seen[target-num],i]) # If yes, return a list with the index of the complement and the current index
            elif num not in seen: # If yes, return a list with the index of the complement and the current index
                seen[num] =i# Add the current number and its index to the seen dictionary
        # If the loop ends without finding a pair, return None implicitl





