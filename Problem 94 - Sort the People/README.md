# 2418. Sort the People

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/sort-the-people/description/)

---

## Problem Description

You are given an array of strings `names`, and an array `heights` that consists of **distinct** positive integers. Both arrays are of length `n`.

For each index `i`, `names[i]` and `heights[i]` denote the name and height of the `ith` person.

Return `names` sorted in **descending** order by the people's heights.

---

## Examples

**Example 1:**

```
Input: names = ["Mary","John","Emma"], heights = [180,165,170]  
Output: ["Mary","Emma","John"]  
Explanation: Mary is the tallest, followed by Emma and John.
```

**Example 2:**

```
Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]  
Output: ["Bob","Alice","Bob"]  
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
```

---

## Constraints

- `n == names.length == heights.length`  
- `1 <= n <= 10³`  
- `1 <= names[i].length <= 20`  
- `1 <= heights[i] <= 10⁵`  
- `names[i]` consists of lower and upper case English letters.  
- All the values of `heights` are distinct.

---

## Solution Strategy

To solve this problem, I used a **hash map for relationship mapping** followed by **sorting**:

1. **Map Relationships**: Since heights are distinct, I created a hash map (dictionary `d`) to map each person's height directly to their name (`d[heights[i]] = names[i]`). Wait, no need to pair indices if the map is available!
2. **Sort**: Reordered the `heights` array in descending order using `.sort(reverse=True)`.
3. **Reconstruct**: Iterated through the freshly sorted `heights` array, fetching the corresponding name for each height from the map and appending it to a result list `res`.
4. **Return**: The ordered list of names.

### Why This Approach?

Dictionary mapping perfectly associates heights with names in O(1) expected time, decoupling the sorting process from multi-attribute array zipping.
- **Time Complexity:** O(N log N) — Establishing the dictionary takes linear time `O(N)`, but sorting the `heights` array dominates at `O(N log N)`. Finally, collecting names takes `O(N)`.
- **Space Complexity:** O(N) — Extra space is consumed by the hash map associating heights to names and the generated resulting list of size `n`.

Because the problem guarantees all height values are strictly distinct, mapping `height -> name` is completely collision-free, ensuring the dictionary technique works flawlessly.

---
