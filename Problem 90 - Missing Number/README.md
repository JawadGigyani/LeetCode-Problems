# 268. Missing Number

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/missing-number/)

---

## Problem Description

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

---

## Examples

**Example 1:**

```
Input: nums = [3,0,1]  
Output: 2  
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
```

**Example 2:**

```
Input: nums = [0,1]  
Output: 2  
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
```

**Example 3:**

```
Input: nums = [9,6,4,2,3,5,7,0,1]  
Output: 8  
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
```

---

## Constraints

- `n == nums.length`  
- `1 <= n <= 10⁴`  
- `0 <= nums[i] <= n`  
- All the numbers of `nums` are **unique**.

---

## Solution Strategy

To solve this problem, I used a **math formulation (Gauss's Summation)** approach:

1. **Calculate Expected Sum**: The array is supposed to contain all numbers from `0` to `n`. The sum of the first `n` natural numbers can be found using the formula `n * (n + 1) // 2`.
2. **Calculate Actual Sum**: Find the sum of the elements present in the `nums` array using Python's built-in `sum()` function.
3. **Find the Difference**: Subtract the actual sum from the expected sum. The difference will be exactly the value of the missing number.
4. **Return** the difference.

### Why This Approach?

Using math turns a potential search problem into a simple arithmetic operation:
- **Time Complexity:** O(n) — The `sum(nums)` function takes linear time to traverse the array once. The math operations take O(1) time.
- **Space Complexity:** O(1) — We only store a couple of integer variables (`expected` sum), requiring constant extra space.

This is highly efficient and directly addresses the problem without needing sorting (which would be O(n log n)) or using a hash set (which would take O(n) space).

---
