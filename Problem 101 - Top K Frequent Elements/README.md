# 347. Top K Frequent Elements

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/top-k-frequent-elements/)

---

## Problem Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

---

## Examples

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2  
Output: [1,2]  
```

**Example 2:**

```
Input: nums = [1], k = 1  
Output: [1]  
```

**Example 3:**

```
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2  
Output: [1,2]  
```

---

## Constraints

- `1 <= nums.length <= 10⁵`  
- `-10⁴ <= nums[i] <= 10⁴`  
- `k` is in the range `[1, the number of unique elements in the array]`.  
- It is guaranteed that the answer is unique.

---

## Solution Strategy

To solve this problem, I used a **frequency counting with sorted extraction** approach:

1. **Edge Case**: If the array has 2 or fewer elements, return the unique elements directly using `set(nums)`.
2. **Count Frequencies**: Use `Counter(nums)` to build a frequency map of all elements.
3. **Sort by Frequency**: Sort the frequency map items in **descending order** by count using `sorted()` with `key=lambda x: x[1]` and `reverse=True`.
4. **Extract Top K**: Iterate through the first `k` entries of the sorted list and collect the element values (not the counts) into a result list.
5. **Return** the result list.

### Why This Approach?

Sorting the frequency pairs gives direct access to the top k elements:
- **Time Complexity:** O(n + u log u) — Counting takes O(n), sorting the u unique elements takes O(u log u), and extracting the top k takes O(k). In the worst case this simplifies to O(n log n).
- **Space Complexity:** O(n) — The frequency map and sorted list scale with the number of unique elements.
