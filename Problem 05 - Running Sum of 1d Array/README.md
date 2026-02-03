# 1480. Running Sum of 1d Array

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/running-sum-of-1d-array/)

---

## Problem Description

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

Return the running sum of `nums`.

---

## Examples

**Example 1:**

```
Input: nums = [1,2,3,4]  
Output: [1,3,6,10]  
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

**Example 2:**

```
Input: nums = [1,1,1,1,1]  
Output: [1,2,3,4,5]  
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
```

**Example 3:**

```
Input: nums = [3,1,2,10,1]  
Output: [3,4,6,16,17]
```

---

## Constraints

- `1 <= nums.length <= 1000`  
- `-10^6 <= nums[i] <= 10^6`

---

## Solution Strategy

To solve this problem, I used an **in-place prefix sum** approach:

1. **Start from the second element** (index 1) since the first element's running sum is itself.
2. **Iterate through the array** and update each element:
   - Add the previous element's value to the current element: `nums[i] = nums[i] + nums[i-1]`
   - This accumulates the sum as we progress through the array
3. **Return the modified array** which now contains the running sums.

### Why This Approach?

This in-place modification is both simple and efficient:
- **Time Complexity:** O(n) - We iterate through the array once
- **Space Complexity:** O(1) - We modify the array in-place without using extra space

Each element becomes the sum of all elements up to and including itself, which is exactly the definition of a running sum. By building on the previous element's cumulative sum, we avoid redundant calculations.

---
