# 13. Roman to Integer

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/roman-to-integer/description/)

---

## Problem Description

Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are usually written largest to smallest from left to right. However, subtraction is used in six cases:

- `I` before `V` (5) and `X` (10) → 4 and 9
- `X` before `L` (50) and `C` (100) → 40 and 90
- `C` before `D` (500) and `M` (1000) → 400 and 900

Given a roman numeral, convert it to an integer.

---

## Examples

**Example 1:**

```
Input: s = "III"  
Output: 3  
Explanation: III = 3.
```

**Example 2:**

```
Input: s = "LVIII"  
Output: 58  
Explanation: L = 50, V = 5, III = 3.
```

**Example 3:**

```
Input: s = "MCMXCIV"  
Output: 1994  
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

---

## Constraints

- `1 <= s.length <= 15`  
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.  
- It is guaranteed that `s` is a valid roman numeral in the range `[1, 3999]`.

---

## Solution Strategy

To solve this problem, I used a **hash map with subtraction rule** approach:

1. **Create a mapping** of Roman symbols to their integer values
2. **Initialize** `total = 0`
3. **Iterate through the string**:
   - If the current symbol's value is **less than** the next symbol's value → **subtract** it (subtraction case)
   - Otherwise → **add** it
4. **Return** `total`.

### Why This Approach?

The subtraction rule is elegantly handled by comparing adjacent values:
- **Time Complexity:** O(n) - We traverse the string once
- **Space Complexity:** O(1) - The hash map has a fixed size of 7 entries

The key insight is that in valid Roman numerals, a smaller value before a larger value always means subtraction (e.g., `IV` = -1 + 5 = 4). Otherwise, values are added normally.

---
