# 350. Intersection of Two Arrays II

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/intersection-of-two-arrays-ii/description/)

---

## Problem Description

Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

---

## Examples

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]  
Output: [2,2]
```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]  
Output: [4,9]  
Explanation: [9,4] is also accepted.
```

---

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`  
- `0 <= nums1[i], nums2[i] <= 1000`

---

## Solution Strategy

To solve this problem, I used a **hash map (Counter)** approach:

1. **Count frequencies** of all elements in `nums1` using `Counter`
2. **Initialize an empty result list**
3. **Iterate through `nums2`**:
   - If the current number has a count greater than 0 in the counter:
     - Add it to the result
     - Decrement the count by 1 (to handle duplicates correctly)
4. **Return** the result list.

### Why This Approach?

Using a Counter efficiently tracks element frequencies:
- **Time Complexity:** O(n + m) - Where n and m are the lengths of `nums1` and `nums2`
- **Space Complexity:** O(n) - The Counter stores frequencies of `nums1`

By decrementing the count each time we find a match, we ensure each element appears in the result only as many times as it exists in both arrays.

---
