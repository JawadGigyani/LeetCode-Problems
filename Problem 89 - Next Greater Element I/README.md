# 496. Next Greater Element I

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/next-greater-element-i/description/)

---

## Problem Description

The **next greater element** of some element `x` in an array is the **first greater** element that is to the right of `x` in the same array.

You are given two **distinct 0-indexed** integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the **next greater element** of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return an array `ans` of length `nums1.length` such that `ans[i]` is the **next greater element** as described above.

---

## Examples

**Example 1:**

```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]  
Output: [-1,3,-1]  
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
```

**Example 2:**

```
Input: nums1 = [2,4], nums2 = [1,2,3,4]  
Output: [3,-1]  
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
```

---

## Constraints

- `1 <= nums1.length <= nums2.length <= 1000`  
- `0 <= nums1[i], nums2[i] <= 10⁴`  
- All integers in `nums1` and `nums2` are **unique**.  
- All the integers of `nums1` also appear in `nums2`.

---

## Solution Strategy

To solve this problem, I used a **monotonic stack with a hash map** approach:

1. **Initialize** an empty `stack` (to keep track of elements whose next greater element is not yet found) and a `next_greater` hash map (to store mappings from an element to its next greater element).
2. **Iterate** through `nums2`:
   - While the `stack` is not empty and the top of the stack is **less than** the current `num`, it means `num` is the next greater element for the element at the top of the stack.
   - Pop elements from the stack, and map them to `num` in the `next_greater` dictionary.
   - Now, append the current `num` to the stack.
3. **Handle remaining items**: After iterating through `nums2`, any element left in the `stack` doesn't have a next greater element to its right. We pop them out and set their value in `next_greater` to `-1`.
4. **Build the result**: Using list comprehension, map each number in `nums1` using the `next_greater` hash map to get the list of final answers.

### Why This Approach?

The monotonic stack technique allows finding the next greater elements for every number in an array in linear time:
- **Time Complexity:** O(M + N) — `M` is the length of `nums2` and `N` is the length of `nums1`. Each element in `nums2` is pushed to and popped from the stack at most once. Building the result for `nums1` takes sequential lookups, which are O(1) each time.
- **Space Complexity:** O(M) — We store elements of `nums2` in a stack and their results in a hash map, both linearly scaling with `nums2`'s size.

This avoids an O(N * M) brute-force nested loop search since you resolve "pending" smaller elements efficiently as higher ones are encountered.

---
