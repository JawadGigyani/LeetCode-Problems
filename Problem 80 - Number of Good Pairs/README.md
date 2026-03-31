# 1512. Number of Good Pairs

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/number-of-good-pairs/description/)

---

## Problem Description

Given an array of integers `nums`, return the number of **good pairs**.

A pair `(i, j)` is called good if `nums[i] == nums[j]` and `i < j`.

---

## Examples

**Example 1:**

```
Input: nums = [1,2,3,1,1,3]  
Output: 4  
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
```

**Example 2:**

```
Input: nums = [1,1,1,1]  
Output: 6  
Explanation: Each pair in the array are good.
```

**Example 3:**

```
Input: nums = [1,2,3]  
Output: 0  
```

---

## Constraints

- `1 <= nums.length <= 100`  
- `1 <= nums[i] <= 100`

---

## Solution Strategy

To solve this problem, I used a **frequency counting in a single pass** approach:

1. **Initialize** an empty dictionary `freq` and a counter `count = 0`
2. **Iterate** through each number `num` in the array:
   - **Add** `freq.get(num, 0)` to `count` — this is the number of previously seen occurrences of `num`, each of which forms a good pair with the current element
   - **Update** the frequency: `freq[num] = freq.get(num, 0) + 1`
3. **Return** `count`.

### Why This Approach?

The key insight is that when we encounter a number that has already appeared `k` times, it forms `k` new good pairs (one with each previous occurrence). By counting on the fly, we avoid the need for a nested loop:
- **Time Complexity:** O(n) — One pass through the array
- **Space Complexity:** O(n) — Dictionary to store frequencies

A brute-force O(n²) approach checking all pairs would also work given the small constraints, but the frequency map approach is cleaner and scales better.

---
