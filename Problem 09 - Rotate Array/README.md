# 189. Rotate Array

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/rotate-array/description/)

---

## Problem Description

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

---

## Examples

**Example 1:**

```
Input: nums = [1,2,3,4,5,6,7], k = 3  
Output: [5,6,7,1,2,3,4]  
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**

```
Input: nums = [-1,-100,3,99], k = 2  
Output: [3,99,-1,-100]  
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

---

## Constraints

- `1 <= nums.length <= 10^5`  
- `-2^31 <= nums[i] <= 2^31 - 1`  
- `0 <= k <= 10^5`

---

## Solution Strategy

To solve this problem, I used an **iterative insert-and-pop** approach:

1. **Get the length** of the array: `n = len(nums)`
2. **Repeat `k` times**:
   - Take the last element of the array (`nums[n-1]`)
   - Insert it at the beginning of the array (`nums.insert(0, ...)`)
   - Remove the last element (`nums.pop()`) to maintain the array size
3. The array is modified **in-place** as required by the problem.

### Why This Approach?

This approach simulates the rotation step by step:
- **Time Complexity:** O(k × n) - Each insert at position 0 takes O(n) time, repeated k times
- **Space Complexity:** O(1) - We modify the array in-place without extra space

While this solution is intuitive and easy to understand, note that there are more efficient approaches using array reversal that achieve O(n) time complexity. However, this straightforward method clearly demonstrates the rotation concept.

---
