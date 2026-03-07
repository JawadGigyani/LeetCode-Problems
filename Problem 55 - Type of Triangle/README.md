# 3024. Type of Triangle

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/type-of-triangle/description/)

---

## Problem Description

You are given a 0-indexed integer array `nums` of size 3 which can form the sides of a triangle.

- A triangle is called **equilateral** if it has all sides of equal length.
- A triangle is called **isosceles** if it has exactly two sides of equal length.
- A triangle is called **scalene** if all its sides are of different lengths.

Return a string representing the type of triangle that can be formed or `"none"` if it cannot form a triangle.

---

## Examples

**Example 1:**

```
Input: nums = [3,3,3]  
Output: "equilateral"  
Explanation: Since all the sides are of equal length, it will form an equilateral triangle.
```

**Example 2:**

```
Input: nums = [3,4,5]  
Output: "scalene"  
Explanation: The sum of any two sides is greater than the third side, and all sides are different lengths.
```

---

## Constraints

- `nums.length == 3`  
- `1 <= nums[i] <= 100`

---

## Solution Strategy

To solve this problem, I used a **direct classification** approach:

1. **Unpack** the sides: `a, b, c = nums`
2. **Triangle inequality check**: If `a + b > c` and `b + c > a` and `c + a > b` is not satisfied, return `"none"`
3. **Classify the triangle**:
   - If `a == b == c` → `"equilateral"`
   - If any two sides are equal (`a == b` or `b == c` or `c == a`) → `"isosceles"`
   - Otherwise → `"scalene"`

### Why This Approach?

Simple conditional checks cover all cases:
- **Time Complexity:** O(1) - Fixed number of comparisons
- **Space Complexity:** O(1) - Only using three variables

The triangle inequality theorem is checked first to handle invalid triangles. Then a cascade of equality checks classifies the type from most restrictive (equilateral) to least (scalene).

---
