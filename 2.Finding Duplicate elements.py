#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Example 1:

#Input: nums = [1,2,3,1]
#Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create a list named unique_numbers
        unique_numbers=set()
        #for taking all values use for loop
        for num in nums:
             # If the element is already in the set, it's a duplicate
            if num in unique_numbers:
                return True
                # Otherwise, add it to the set
            unique_numbers.add(num)
            # No duplicates found
            
        return False
