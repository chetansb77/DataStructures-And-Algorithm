""" PROBLEM STATEMENT: VALID PALIDROME
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
    it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Example 1:
        Input: s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2:
        Input: s = "race a car"
        Output: false
        Explanation: "raceacar" is not a palindrome.

    Example 3:
        Input: s = " "
        Output: true
        Explanation: s is an empty string "" after removing non-alphanumeric characters.
        Since an empty string reads the same forward and backward, it is a palindrome.
 

    Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""

""" PSEUDO CODE SOLUTION

SIMPLE SOLUTION: (REVERSE STRING AND COMPARE)
    - loop through the characters of the string
        - filter if the character is alpha-numeric
        - lowercase the character
    - Compare the filtered string with its reversed string
        - IF same - return TRUE
        - IF not same - return FALSE
        
    TIME COMPLEXITY: O(n) (Best case and worst case)
        - because we loop through the ARRAY
    SPACE COMPLEXITY: O(n)
        - string of the same length is created for the reverse string
        

BEST APPROACH: (USING TWO POINTERS)
    - Create two pointers
        - left pointer for beginning of the string
        - right pointer at the end of the string
    - While left < right
        - check if left pointer character is alpha-numeric
            - if no - increment left pointer by 1 and check again ( do until left = right)
            - if yes continue
        - check if right pointer character is alpha-numeric
            - if no - decrement right pointer by 1 and check again ( do until left = right)
            - if yes continue
        - check if character at left pointer is same as character in right pointer (case-insensitive)
            - if NO - return FALSE
            - if YES - increament left by 1 and decreament right by 1
    - IF while loop completes - retun TRUE
    
    TIME COMPLEXITY: O(1)(Best case) O(n)(Worst case)
        - because we loop through the ARRAY
    SPACE COMPLEXITY: O(1)
        - constant space used
"""

def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum(): 
            l += 1
        while l < r and not s[r].isalnum(): 
            r -= 1
        if s[l].lower() != s[r].lower(): 
            return False
        l += 1
        r -= 1
    return True