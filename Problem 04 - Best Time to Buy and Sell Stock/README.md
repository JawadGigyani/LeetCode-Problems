# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

## Problem Description

Given an array `prices` where `prices[i]` is the price of a given stock on the i<sup>th</sup> day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

---

## Examples

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]  
Output: 5  
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**

```
Input: prices = [7,6,4,3,1]  
Output: 0  
Explanation: In this case, no transactions are done and the max profit = 0.
```

---

## Constraints

- `1 <= prices.length <= 10^5`  
- `0 <= prices[i] <= 10^4`

---

## Solution Strategy

To solve this problem, I used a **sliding window** approach that tracks the minimum price and maximum profit:

1. **Initialize two variables**:
   - `min_price` to track the lowest price seen so far (initially set to infinity)
   - `max_profit` to track the maximum profit achievable (initially set to 0)
2. **Iterate through each price** in the array:
   - Update `min_price` if the current price is lower than the minimum seen so far
   - Calculate the potential profit by selling at the current price: `profit = current_price - min_price`
   - Update `max_profit` if this profit is greater than the current maximum
3. **Return** the `max_profit` after processing all prices.

### Why This Approach?

This single-pass algorithm efficiently finds the optimal buy and sell days:
- **Time Complexity:** O(n) - We iterate through the array once
- **Space Complexity:** O(1) - We only use two variables regardless of input size

The key insight is that we always want to buy at the lowest price before selling, so tracking the minimum price as we go allows us to calculate the best possible profit at each step without needing nested loops.

---
