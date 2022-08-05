""" PROBLEM STATEMENT: Binary Search
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
    If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
        Input: nums = [-1,0,3,5,9,12], target = 9
        Output: 4
        Explanation: 9 exists in nums and its index is 4
    
    Example 2:
        Input: nums = [-1,0,3,5,9,12], target = 2
        Output: -1
        Explanation: 2 does not exist in nums so return -1
    

    Constraints:
        1 <= nums.length <= 104
        -104 < nums[i], target < 104
        All the integers in nums are unique.
        nums is sorted in ascending order.
"""

""" PSEUDO CODE SOLUTION

SOLUTION: (BINARY SEARCH (DIVIDE AND CONQUOR))
    - Initialize LEFT and RIGHT pointers
    - while LEFT <= RIGHT
        - find MID index
        - check if target is equal to MID value
            - Return MID index if TRUE
        - Else if target is less than MID, RIGHT is MID - 1
        - Else if target is greater that MID, LEFT is MID + 1
    - if LEFT >= RIGHT
        -return -1
    
"""

import math
from typing import List

def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target >= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1
        