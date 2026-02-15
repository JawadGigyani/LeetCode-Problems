# 1004. Max Consecutive Ones III

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/max-consecutive-ones-iii/description/)

---

## Problem Description

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s.

---

## Examples

**Example 1:**

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2  
Output: 6  
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

**Example 2:**

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3  
Output: 10  
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

---

## Constraints

- `1 <= nums.length <= 10^5`  
- `nums[i]` is either `0` or `1`.  
- `0 <= k <= nums.length`

---

## Solution Strategy

To solve this problem, I used a **sliding window** approach:

1. **Initialize**: `left = 0`, `count = 0` (tracks zeroes in the window), `max_ones = 0`
2. **Expand the window** by moving `right` through the array:
   - If `nums[right] == 0`, increment `count`
3. **Shrink the window** when `count > k` (too many zeroes to flip):
   - If `nums[left] == 0`, decrement `count`
   - Move `left` forward
4. **Update** `max_ones` with the current window size: `right - left + 1`
5. **Return** `max_ones`.

### Why This Approach?

The sliding window efficiently finds the longest subarray with at most k zeroes:
- **Time Complexity:** O(n) - Each element is visited at most twice (once by each pointer)
- **Space Complexity:** O(1) - Only using a few variables

The window maintains the invariant that it contains at most `k` zeroes. When a new zero would exceed the limit, we shrink from the left until we're back within bounds.

---
