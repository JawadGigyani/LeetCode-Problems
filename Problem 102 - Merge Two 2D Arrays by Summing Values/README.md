# 2570. Merge Two 2D Arrays by Summing Values

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/)

---

## Problem Description

You are given two 2D integer arrays `nums1` and `nums2`.

- `nums1[i] = [idᵢ, valᵢ]` indicate that the number with the id `idᵢ` has a value equal to `valᵢ`.
- `nums2[i] = [idᵢ, valᵢ]` indicate that the number with the id `idᵢ` has a value equal to `valᵢ`.

Each array contains **unique** ids and is sorted in **ascending order** by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

- Only ids that appear in at least one of the two arrays should be included in the resulting array.
- Each id should be included **only once** and its value should be the **sum** of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be `0`.

Return the resulting array. The returned array must be sorted in ascending order by id.

---

## Examples

**Example 1:**

```
Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]  
Output: [[1,6],[2,3],[3,2],[4,6]]  
Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.
```

**Example 2:**

```
Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]  
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]  
Explanation: There are no common ids, so we just include each id with its value in the resulting list.
```

---

## Constraints

- `1 <= nums1.length, nums2.length <= 200`  
- `nums1[i].length == nums2[j].length == 2`  
- `1 <= idᵢ, valᵢ <= 1000`  
- Both arrays contain unique ids.  
- Both arrays are in strictly ascending order by id.

---

## Solution Strategy

To solve this problem, I used a **two-pointer merge** approach (similar to merge sort's merge step):

1. **Initialize** two pointers `i = j = 0` and an empty result list `res`
2. **Merge While Both Have Elements**: While both pointers are within bounds:
   - **Equal IDs**: If `nums1[i][0] == nums2[j][0]`, sum the values and append `[id, sum]` to `res`. Advance both pointers.
   - **nums1 ID is smaller**: Append `nums1[i]` to `res` and advance `i`.
   - **nums2 ID is smaller**: Append `nums2[j]` to `res` and advance `j`.
3. **Append Remaining**: After the loop, extend `res` with any leftover elements from whichever array hasn't been fully traversed.
4. **Return** `res`.

### Why This Approach?

Since both arrays are pre-sorted by id, the two-pointer technique merges them optimally in a single pass:
- **Time Complexity:** O(n + m) — Where n and m are the lengths of `nums1` and `nums2`. Each element is processed exactly once.
- **Space Complexity:** O(n + m) — The result array stores at most n + m entries.

