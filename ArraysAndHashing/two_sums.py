""" PROBLEM STATEMENT: TWO SUMS

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    
    Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]
    
    Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]

    Constraints:
        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        Only one valid answer exists.
"""


""" PSEUDOCODE: 

SIMPLE SOLUTION - BRUTE FORCE using TWO NESTED FOR LOOPS
    - Loop through every element in the ARRAY - iterator i
        - Loop through every element in the ARRAY from i+1 - iterator j
            - Chech if element i + element j == target
                - IF YES - return [i, j]
                
    TIME COMPLEXITY: O(n^2)
        - Two nested for loops
    SPACE COMPLEXITY: O(1)
        - no additional space required
        
        
BEST APPROACH - HASH MAP
    - Create a HASH MAP(dict)
    - Loop through the array - iterator i
        - check if array[i] is a hash key
            - IF NO 
                - get difference: target - array[i]
                - add difference value as a hash key with value as index i
            - IF YES
                - return [hash[array[i]], i]
    
    TIME COMPLEXITY: O(n)
        - looping array once
    SPACE COMPLEXITY: O(n)
        - creating hash map
""" 

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    
    hash_set = dict()
    
    for i, value in enumerate(nums):
        if value in hash_set.keys():
            return [hash_set[value], i]
        else:
            hash_set[target - value] = i