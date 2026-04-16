# 2956. Find Common Elements Between Two Arrays

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/find-common-elements-between-two-arrays/description/)

---

## Problem Description

You are given two integer arrays `nums1` and `nums2` of sizes `n` and `m`, respectively. Calculate the following values:

- `answer1`: the number of indices `i` such that `nums1[i]` exists in `nums2`.
- `answer2`: the number of indices `i` such that `nums2[i]` exists in `nums1`.

Return `[answer1, answer2]`.

---

## Examples

**Example 1:**

```
Input: nums1 = [2,3,2], nums2 = [1,2]  
Output: [2,1]  
Explanation:  
```
![Find Common Elements Between Two Arrays](https://assets.leetcode.com/uploads/2024/05/26/3488_find_common_elements_between_two_arrays-t1.gif)

**Example 2:**

```
Input: nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]  
Output: [3,4]  
Explanation:
The elements at indices 1, 2, and 3 in nums1 exist in nums2 as well. So answer1 is 3.
The elements at indices 0, 1, 3, and 4 in nums2 exist in nums1. So answer2 is 4.
```

**Example 3:**

```
Input: nums1 = [3,4,2,3], nums2 = [1,5]  
Output: [0,0]  
Explanation:
No numbers are common between nums1 and nums2, so answer is [0,0].
```

---

## Constraints

- `n == nums1.length`
- `m == nums2.length`
- `1 <= n, m <= 100`
- `1 <= nums1[i], nums2[i] <= 100`

---

## Solution Strategy

To solve this problem efficiently, I used a **hash set lookup** approach:

1. **Convert to Sets:** Convert both `nums1` and `nums2` into sets (`set1` and `set2`). This allows for $O(1)$ average-case time complexity when checking if an element exists.
2. **Count Common Elements in `nums1`:** Iterate through each element in the array `nums1`. For each element, check if it exists in `set2`. Sum the occurrences where this condition holds to get `answer1`.
3. **Count Common Elements in `nums2`:** Iterate through each element in the array `nums2`. For each element, check if it exists in `set1`. Sum the occurrences where this condition holds to get `answer2`.
4. **Return Results:** Return the calculated values as a list `[count1, count2]`.

### Why This Approach?

Using sets optimizes the search process:
- **Time Complexity:** $O(n + m)$ — Creating the sets takes $O(n)$ and $O(m)$ time respectively. Iterating through `nums1` to check against `set2` takes $O(n)$ time, and iterating through `nums2` to check against `set1` takes $O(m)$ time. This is much faster than the $O(n \times m)$ brute-force approach.
- **Space Complexity:** $O(n + m)$ — Storing the unique elements of `nums1` and `nums2` in sets requires additional space proportional to the number of distinct elements in the corresponding arrays, which in the worst case is $O(n + m)$.

This Python implementation leverages list comprehensions (or generator expressions) with `sum()` for a clean and remarkably concise solution.
