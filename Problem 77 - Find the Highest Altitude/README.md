# 1732. Find the Highest Altitude

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/find-the-highest-altitude/description/)

---

## Problem Description

There is a biker going on a road trip. The road trip consists of `n + 1` points at different altitudes. The biker starts his trip on point `0` with altitude equal `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the net gain in altitude between points `i` and `i + 1` for all `(0 <= i < n)`. Return the **highest altitude** of a point.

---

## Examples

**Example 1:**

```
Input: gain = [-5,1,5,0,-7]  
Output: 1  
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
```

**Example 2:**

```
Input: gain = [-4,-3,-2,-1,4,3,2]  
Output: 0  
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
```

---

## Constraints

- `n == gain.length`  
- `1 <= n <= 100`  
- `-100 <= gain[i] <= 100`

---

## Solution Strategy

To solve this problem, I used a **prefix sum with running maximum** approach:

1. **Initialize** `curr_alt = 0` (starting altitude) and `max_alt = 0` (highest seen so far)
2. **Iterate** through each gain value `g`:
   - **Accumulate** the altitude: `curr_alt += g`
   - **Update** the maximum: `max_alt = max(max_alt, curr_alt)`
3. **Return** `max_alt`.

### Why This Approach?

The altitudes are simply the prefix sums of the `gain` array, so we only need a single pass:
- **Time Complexity:** O(n) — One pass through the gain array
- **Space Complexity:** O(1) — Only two variables are used

Note that `max_alt` starts at `0` (not negative infinity) because the starting altitude is `0` and must be considered as a candidate for the highest point — as seen in Example 2 where the answer is `0`.

---
