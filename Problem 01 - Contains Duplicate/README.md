# 217. Contains Duplicate

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/contains-duplicate/)

---

## Problem Description

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---

## Examples

**Example 1:**

```
Input: nums = [1,2,3,1]  
Output: true  
Explanation: The element 1 occurs at the indices 0 and 3.
```

**Example 2:**

```
Input: nums = [1,2,3,4]  
Output: false  
Explanation: All elements are distinct.
```

**Example 3:**

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]  
Output: true
```

---

## Constraints

- `1 <= nums.length <= 10^5`  
- `-10^9 <= nums[i] <= 10^9`

---

## Solution Strategy

To solve this problem, I used a **hash set** approach for optimal performance:

1. **Create an empty set** called `unique` to track elements we've seen.
2. **Iterate through each element** in the array:
   - If the element already exists in the set, we've found a duplicate → return `True`
   - Otherwise, add the element to the set
3. If the loop completes without finding duplicates, return `False`.

### Why This Approach?

Using a set allows for **O(1)** average-case lookup time, making this solution very efficient:
- **Time Complexity:** O(n) - We iterate through the array once
- **Space Complexity:** O(n) - In the worst case, we store all unique elements in the set

This is more efficient than sorting (O(n log n)) when we only need to detect the presence of duplicates.

---
