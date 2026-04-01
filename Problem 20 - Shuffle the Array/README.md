# 1470. Shuffle the Array

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/shuffle-the-array/description/)

---

## Problem Description

Given the array `nums` consisting of `2n` elements in the form `[x1,x2,...,xn,y1,y2,...,yn]`.

Return the array in the form `[x1,y1,x2,y2,...,xn,yn]`.

---

## Examples

**Example 1:**

```
Input: nums = [2,5,1,3,4,7], n = 3  
Output: [2,3,5,4,1,7]  
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
```

**Example 2:**

```
Input: nums = [1,2,3,4,4,3,2,1], n = 4  
Output: [1,4,2,3,3,2,4,1]
```

**Example 3:**

```
Input: nums = [1,1,2,2], n = 2  
Output: [1,2,1,2]
```

---

## Constraints

- `1 <= n <= 500`  
- `nums.length == 2n`  
- `1 <= nums[i] <= 10^3`

---

## Solution Strategy (In-Place Insert-and-Delete)

To solve this problem, I first used an **in-place insert-and-delete** approach:

1. **Initialize pointer** `l = 1` (the position where the first y-element should go)
2. **Loop while `l < len(nums)`**:
   - **Insert** the element at index `n` into position `l` (`nums.insert(l, nums[n])`)
   - Increment `n` by 1 (since the insert shifted elements right)
   - **Delete** the original element at index `n` (`del nums[n]`)
   - Move `l` forward by 2 (`l += 2`) to skip to the next interleave position
3. **Return** the modified array.

### Why This Approach?

This approach interleaves the two halves by moving elements from the second half into their correct positions:
- **Time Complexity:** O(n²) — Each insert/delete operation shifts elements
- **Space Complexity:** O(1) — We modify the array in-place

The pointer `l` jumps by 2 each iteration because after placing a y-element, the next y-element goes two positions ahead (after the next x-element).

---

## Improved Solution (List Comprehension)

I later revisited this problem with a cleaner **list comprehension** approach:

1. **Iterate** `i` from `0` to `n - 1`
2. For each `i`, **yield** the pair `(nums[i], nums[i + n])` — pairing up the corresponding x and y elements
3. The nested comprehension **flattens** these pairs into a single list.

```python
return [num for i in range(n) for num in (nums[i], nums[i+n])]
```

### Why This Improvement?

The original solution works, but the repeated `insert` and `del` operations each cost O(n) due to element shifting, making it O(n²) overall. The list comprehension approach directly builds the result by pairing `nums[i]` with `nums[i + n]`:
- **Time Complexity:** O(n) — Single pass through the first half, each pair lookup is O(1)
- **Space Complexity:** O(n) — A new list is constructed for the result

It trades the in-place advantage for a much cleaner and faster solution. Given that we need to return a list anyway, the O(n) space is perfectly acceptable and the readability gain is significant.

---
