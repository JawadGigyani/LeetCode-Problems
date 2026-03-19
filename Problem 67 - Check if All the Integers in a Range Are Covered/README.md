# 1893. Check if All the Integers in a Range Are Covered

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/)

---

## Problem Description

You are given a 2D integer array `ranges` and two integers `left` and `right`. Each `ranges[i] = [startᵢ, endᵢ]` represents an inclusive interval between `startᵢ` and `endᵢ`.

Return `true` if each integer in the inclusive range `[left, right]` is covered by at least one interval in `ranges`. Return `false` otherwise.

An integer `x` is covered by an interval `ranges[i] = [startᵢ, endᵢ]` if `startᵢ <= x <= endᵢ`.

---

## Examples

**Example 1:**

```
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5  
Output: true  
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.
```

**Example 2:**

```
Input: ranges = [[1,10],[10,20]], left = 21, right = 21  
Output: false  
Explanation: 21 is not covered by any range.
```

---

## Constraints

- `1 <= ranges.length <= 50`  
- `1 <= startᵢ <= endᵢ <= 50`  
- `1 <= left <= right <= 50`

---

## Solution Strategy

To solve this problem, I used a **sort and sweep** approach:

1. **Sort** the `ranges` by their start values
2. **Initialize** a pointer `curr = left` representing the next integer that needs to be covered
3. **Iterate** through each `[start, end]` in the sorted ranges:
   - If `start <= curr`, the current range can cover `curr` — advance `curr` to `end + 1`
   - If `curr > right`, all integers are already covered — return `True` early
4. **After the loop**, return `curr > right` to check if full coverage was achieved.

### Why This Approach?

Sorting by start value lets us greedily extend coverage from left to right:
- **Time Complexity:** O(n log n) — Dominated by the sort step
- **Space Complexity:** O(1) — Only a single pointer `curr` is used (excluding sort space)

By sweeping through sorted intervals, each range either extends our covered region or is skipped. If at any point `curr` surpasses `right`, we know the entire `[left, right]` range is covered.

---
