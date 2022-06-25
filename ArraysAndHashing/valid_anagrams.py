""" PROBLEM STATEMENT: VALID ANAGRAMS

    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Example 1:
        Input: s = "anagram", t = "nagaram"
        Output: true
    
    Example 2:
        Input: s = "rat", t = "car"
        Output: false

    Constraints:
        1 <= s.length, t.length <= 5 * 104
        s and t consist of lowercase English letters.
"""


""" PSEUDOCODE: 

SIMPLE SOLUTION:
    - Check of both the string length is equal
        - If not return FALSE
    - Sort both the string 
    - Check if both the string are equal
        - IF YES - return TRUE
        - IF NO - return FALSE
        
    TIME COMPLEXITY: O(nlogn)
        - because we use sort alogo
    SPACE COMPLEXITY: O(1)
        - no additional space required
        
BEST APPROACH (HASH TABLE):
    - Check of both the string length is equal
        - If not return FALSE
    - Create Two hash tables (dict) hashA hashB
    - Loop through the range of length of any string (as both lenght are same)
        - stringA
            - Check if the letter is in stringA hash table
                - IF NO - add the letter as a key and initialize value by 1
                - IF YES - increase the value by 1
        - stringB
            - Check if the letter is in stringB hash table
                - IF NO - add the letter as a key and initialize value by 1
                - IF YES - increase the value by 1      
    - Loop through each KEY(HASH) of in hashA
        - Check if hash value is same in both hashes
        - if YES - return TRUE
        - if NO - return FALSE
        
    TIME COMPLEXITY: O(n)
        - looping array of lenth once
    SPACE COMPLEXITY: O(n)
        - hash table is created for each array
"""


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True