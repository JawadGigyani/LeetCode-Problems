# 49. Group Anagrams

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/group-anagrams/description/)

---

## Problem Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

---

## Examples

**Example 1:**

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]  
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]  
Explanation:
- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
```

**Example 2:**

```
Input: strs = [""]  
Output: [[""]]
```

**Example 3:**

```
Input: strs = ["a"]  
Output: [["a"]]
```

---

## Constraints

- `1 <= strs.length <= 10^4`  
- `0 <= strs[i].length <= 100`  
- `strs[i]` consists of lowercase English letters.

---

## Solution Strategy

To solve this problem, I used a **sorted key with hash map** approach:

1. **Initialize** a `defaultdict(list)` to group anagrams
2. **Iterate through each word**:
   - Sort the word and convert to a tuple as the `key`
   - Append the original word to `mp[key]`
3. **Return** the values of the hash map as a list.

### Why This Approach?

Sorting each word creates a canonical form that all anagrams share:
- **Time Complexity:** O(n * k log k) - Where n is the number of strings and k is the max string length (sorting each word)
- **Space Complexity:** O(n * k) - Storing all strings in the hash map

Anagrams become identical when sorted (e.g., "eat", "tea", "ate" all become "aet"), making sorted tuples perfect hash map keys for grouping.

---
