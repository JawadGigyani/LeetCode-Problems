# 901. Online Stock Span

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/online-stock-span/description/)

---

## Problem Description

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

Implement the `StockSpanner` class:

- `StockSpanner()` Initializes the object of the class.
- `int next(int price)` Returns the span of the stock's price given that today's price is `price`.

---

## Examples

**Example 1:**

```
Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]

Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4
stockSpanner.next(85);  // return 6
```

---

## Constraints

- `1 <= price <= 10^5`  
- At most `10^4` calls will be made to `next`.

---

## Solution Strategy

To solve this problem, I used a **monotonic stack** approach:

1. **Initialize an empty stack** that stores tuples of `(price, span)`.
2. **For each `next(price)` call**:
   - Start with `span = 1`
   - **While the stack is not empty** and the top element's price is `<= price`:
     - Add the top element's span to our current span
     - Pop the top element from the stack
   - **Push** the current `(price, span)` onto the stack
   - **Return** the calculated span

### Why This Approach?

The monotonic stack efficiently combines spans of smaller prices:
- **Time Complexity:** O(1) amortized per call - Each element is pushed and popped at most once
- **Space Complexity:** O(n) - Stack stores at most n elements

When a new price is higher than previous prices, we absorb their spans into the current one. This avoids recalculating spans from scratch each time. The stack maintains a decreasing order of prices, making it a monotonic decreasing stack.

---
