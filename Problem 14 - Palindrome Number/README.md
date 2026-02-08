# 9. Palindrome Number

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/palindrome-number/description/)

---

## Problem Description

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

---

## Examples

**Example 1:**

```
Input: x = 121  
Output: true  
Explanation: 121 reads as 121 from left to right and from right to left.
```

**Example 2:**

```
Input: x = -121  
Output: false  
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**

```
Input: x = 10  
Output: false  
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

---

## Constraints

- `-2^31 <= x <= 2^31 - 1`

---

## Solution Strategy

To solve this problem, I used a **string reversal** approach:

1. **Convert the integer to a string**: `str(x)`
2. **Reverse the string** using `"".join(reversed(str(x)))`
3. **Compare** the original string with the reversed string:
   - If they are equal, return `True` (it's a palindrome)
   - Otherwise, return `False`

### Why This Approach?

String conversion makes palindrome checking straightforward:
- **Time Complexity:** O(n) - Where n is the number of digits (reversing and comparing strings)
- **Space Complexity:** O(n) - Creating string representations of the number

This approach elegantly handles negative numbers automatically - the minus sign at the beginning will never match the end, so negative numbers correctly return `False`.

---
