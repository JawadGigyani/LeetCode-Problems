# 1984. Minimum Difference Between Highest and Lowest of K Scores

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/)

---

## Problem Description

You are given a 0-indexed integer array `nums`, where `nums[i]` represents the score of the i<sup>th</sup> student. You are also given an integer `k`.

Pick the scores of any `k` students from the array so that the difference between the highest and the lowest of the `k` scores is **minimized**.

Return the minimum possible difference.

---

## Examples

**Example 1:**

```
Input: nums = [90], k = 1  
Output: 0  
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.
```

**Example 2:**

```
Input: nums = [9,4,1,7], k = 2  
Output: 2  
Explanation: There are six ways to pick score(s) of two students.
The minimum possible difference is 2 (picking scores 7 and 9).
```

---

## Constraints

- `1 <= k <= nums.length <= 1000`  
- `0 <= nums[i] <= 10^5`

---

## Solution Strategy

To solve this problem, I used a **sort and sliding window** approach:

1. **Edge case**: If `k <= 1`, return `0` (single element has no difference)
2. **Sort** the array
3. **Slide a window of size k** across the sorted array:
   - For each window starting at index `i`, compute `nums[i+k-1] - nums[i]`
   - Track the minimum difference
4. **Return** the minimum difference.

### Why This Approach?

Sorting ensures the closest values are adjacent, minimizing the window's range:
- **Time Complexity:** O(n log n) - Dominated by the sort
- **Space Complexity:** O(1) - Only using a few variables (excluding sort space)

After sorting, the optimal k elements must be consecutive — any gap would increase the difference. So we just slide a window of size k and find the smallest max-min difference.

---
