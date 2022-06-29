""" PROBLEM STATEMENT: Valid Parentheses

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
        - Open brackets must be closed by the same type of brackets.
        - Open brackets must be closed in the correct order.
    

    Example 1:
        Input: s = "()"
        Output: true
    
    Example 2:
        Input: s = "()[]{}"
        Output: true
    
    Example 3:
        Input: s = "(]"
        Output: false
    

    Constraints:
        1 <= s.length <= 104
        s consists of parentheses only '()[]{}'
"""

""" PSEUDO CODE SOLUTION

BEST APPROACH: USING STACK and DICTIONARY
    - Create a dictionary of keys as the closing brackets ')]}' and respective opening brackets as values
    - Check if the first character in the string is one of the keys
        - IF YES - return FALSE
        - ELSE - add the character to the top of the stack
    - Loop through each character
        - IF character is key
            - Check if the top of the stack is the value of the key
                - If YES - pop the top of the stack
                - If NO - return False
        - ELSE
            - Add the character at the top of the stack
    - IF stack is empty
        - Return TRUE
    - ELSE
        - RETURN FALSE
        
    TIME COMPLEXITY: O(n)
        - because we loop through the ARRAY
    SPACE COMPLEXITY: O(n)
        - stack is used
"""


def valid_parentheses(s: str) -> bool:
    map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    stack = []
    
    if s[0] in map.keys():
        return False
    else:
        stack.append(s[0])
        
    for br in s[1:]:
        if br in map.keys():
            if len(stack) == 0:
                return False
            if stack.pop() == map[br]:
                continue
            else:
                return False
        else:
            stack.append(br)
    
    if len(stack) == 0:
        return True
    else:
        return False
    