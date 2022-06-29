""" PROBLEM STATEMENT: Best Time to Buy and Sell Stock
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Example 1:
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    
    Example 2:
        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transactions are done and the max profit = 0.

    Constraints:
        1 <= prices.length <= 10^5
        0 <= prices[i] <= 10^4

"""

""" PSEUDO CODE SOLUTION

BRUTE FORCE SOLUTION: (TWO NESTED FOR LOOPS)

    TIME COMPLEXITY: O(n^2)
        - because we loop through the ARRAY in nested manner
    SPACE COMPLEXITY: O(1)
        - space is not proportional to the input size
        
        
BEST APPROACH: USING POINTERS
    - Initialize MAX-PROFIT to 0
    - BUY index at 0
    - SELL index at 1
    - If SELL-BUY is greater that MAX-PROFIT: Update Max profit
    - If SELL is LESS that BUY : move BUY pointer to SELL index
    - Return MAX-PROFIT

    TIME COMPLEXITY: O(n)
        - because we loop through the ARRAY once
    SPACE COMPLEXITY: O(1)
        - space is not proportional to the input size
"""


from typing import List


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    buy = prices[0]
    
    for sell in prices[1:]:
        if sell - buy > max_profit:
            max_profit = sell - buy
        elif sell < buy:
            buy = sell
    
    return max_profit