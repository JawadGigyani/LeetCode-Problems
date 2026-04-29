# 2161. Partition Array According to Given Pivot

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/partition-array-according-to-given-pivot/description/)

---

## Problem Description

You are given a 0-indexed integer array `nums` and an integer `pivot`. Rearrange `nums` such that the following conditions are satisfied:

- Every element **less than** `pivot` appears before every element **greater than** `pivot`.
- Every element **equal to** `pivot` appears in between the elements less than and greater than `pivot`.
- The **relative order** of the elements less than `pivot` and the elements greater than `pivot` is maintained.

Return `nums` after the rearrangement.

---

## Examples

**Example 1:**

```
Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
Explanation: 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
```

**Example 2:**

```
Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]
Explanation: 
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.
```

---

## Constraints

- `1 <= nums.length <= 10⁵`
- `-10⁶ <= nums[i] <= 10⁶`
- `pivot` equals to an element of `nums`

---

## Solution Strategy

To solve this problem, I used a **three-bucket partition** approach:

1. **Initialize** three separate lists: `less`, `equal`, and `greater`
2. **Loop** through every `num` in `nums`:
   - If `num < pivot`: append to `less`
   - If `num > pivot`: append to `greater`
   - Otherwise (`num == pivot`): append to `equal`
3. **Concatenate** and return `less + equal + greater`

### Why This Approach?

Splitting into three buckets is the most straightforward way to satisfy all three conditions at once — relative order is preserved naturally since we iterate left to right, and the three groups are assembled in the correct sequence at the end:

- **Time Complexity:** O(n) — A single pass to classify each element, plus O(n) to concatenate the lists
- **Space Complexity:** O(n) — Three auxiliary lists that together hold all `n` elements

The key insight is that maintaining relative order (stability) rules out any in-place swapping approach, since swaps inherently disrupt original ordering. By collecting elements into dedicated buckets in a single forward pass, we guarantee both stability and correct partitioning with minimal code.

---
