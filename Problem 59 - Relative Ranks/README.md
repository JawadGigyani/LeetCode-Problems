# 506. Relative Ranks

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/relative-ranks/description/)

---

## Problem Description

You are given an integer array `score` of size `n`, where `score[i]` is the score of the i<sup>th</sup> athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1<sup>st</sup> place athlete has the highest score. The placement determines their rank:

- 1<sup>st</sup> place → `"Gold Medal"`
- 2<sup>nd</sup> place → `"Silver Medal"`
- 3<sup>rd</sup> place → `"Bronze Medal"`
- 4<sup>th</sup> place and beyond → their placement number as a string

Return an array `answer` where `answer[i]` is the rank of the i<sup>th</sup> athlete.

---

## Examples

**Example 1:**

```
Input: score = [5,4,3,2,1]  
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]  
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
```

**Example 2:**

```
Input: score = [10,3,8,9,4]  
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]  
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
```

---

## Constraints

- `n == score.length`  
- `1 <= n <= 10^4`  
- `0 <= score[i] <= 10^6`  
- All the values in `score` are **unique**.

---

## Solution Strategy

To solve this problem, I used a **max heap with original indices** approach:

1. **Build a max heap**: Store `(-score, index)` tuples (negated for max heap simulation)
2. **Heapify** the list
3. **Pop elements one by one** (highest score first), assigning ranks:
   - Rank 1 → `"Gold Medal"`
   - Rank 2 → `"Silver Medal"`
   - Rank 3 → `"Bronze Medal"`
   - Rank 4+ → convert rank to string
4. **Place each rank** at the athlete's original index in the answer array.

### Why This Approach?

A max heap naturally retrieves athletes in descending score order:
- **Time Complexity:** O(n log n) - Heapify is O(n), n pops each O(log n)
- **Space Complexity:** O(n) - Heap and answer array

By storing original indices alongside scores, we can place ranks directly into the correct positions without losing track of which athlete had which score.

---
