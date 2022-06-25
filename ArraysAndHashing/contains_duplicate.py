""" PROBLEM STATEMENT: CONTAINS DUPLCATES
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    Example 1:
        Input: nums = [1,2,3,1]
        Output: true
        
    Example 2:
        Input: nums = [1,2,3,4]
        Output: false
    
    Example 3:
        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true


    Constraints:
        1 <= nums.length <= 105
        -10^9 <= nums[i] <= 10^9

"""

""" PSEUDO CODE SOLUTION

SIMPLE APPROACH:
    - Perform SET operation on the ARRAY
    - Check if the length of SET == length of ARRAY
    - if YES - ARRAY doesnt have duplicates
    - if NO - ARRAY has duplicates
    
    TIME COMPLEXITY: O(n)
        - because we loop through the ARRAY
    SPACE COMPLEXITY: O(n)
        - order of one, (we create a set)
        
        
BEST APPROACH: (USING HASH SET)
    - Create a hash set
    - Loop through the array
        - Check if item is in hash set
            - If yes - return TRUE
            - If no - add item to the set
    - If loop is completed - return FALSE (as all the items from array was added into hash set)

    TIME COMPLEXITY: O(n)
        - because we loop through the ARRAY
    SPACE COMPLEXITY: O(n)
        - order of one, (we create a set)
"""


from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()
    
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False