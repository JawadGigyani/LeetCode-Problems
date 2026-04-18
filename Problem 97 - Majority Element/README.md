# 169. Majority Element

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/majority-element/description/)

---

## Problem Description

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

---

## Examples

**Example 1:**

```
Input: nums = [3,2,3]  
Output: 3  
```

**Example 2:**

```
Input: nums = [2,2,1,1,1,2,2]  
Output: 2  
```

---

## Constraints

- `n == nums.length`  
- `1 <= n <= 5 * 10⁴`  
- `-10⁹ <= nums[i] <= 10⁹`  
- The input is generated such that a majority element will exist in the array.

---

## Solution Strategy

To solve this problem efficiently in linear time and O(1) space, I used the **Boyer-Moore Voting Algorithm**:

1. **Initialize Tracking Variables:** Maintain a `candidate` tracker (initially `None`) and a `count` (initially `0`).
2. **Iterate Through the Array:** For each number `num` in `nums`:
   - If `count == 0`: We assign the current `num` as our new potential `candidate`.
   - If `num == candidate`: We increment the `count` by `1` (solidifying the candidate's lead).
   - If `num != candidate`: We decrement the `count` by `1` (another element "votes against" the candidate).
3. **Return Candidate:** Because the problem guarantees that a majority element exists (it appears more than `n/2` times), the `count` for the true majority element will eventually outweigh all other elements combined. By the end of the loop, `candidate` will hold the correct answer.

### Why This Approach?

The Boyer-Moore Voting Algorithm is the optimal approach for the majority element problem:
- **Time Complexity:** $O(n)$ — The array is traversed exactly once.
- **Space Complexity:** $O(1)$ — Only two variables (`candidate` and `count`) are stored, regardless of the input array size.

This avoids the $O(n)$ space requirement of using a hash map to count frequencies, and the $O(n \log n)$ time requirement of sorting the array.

