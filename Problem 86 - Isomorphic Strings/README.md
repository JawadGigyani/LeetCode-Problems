# 205. Isomorphic Strings

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/isomorphic-strings/description/)

---

## Problem Description

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

---

## Examples

**Example 1:**

```
Input: s = "egg", t = "add"  
Output: true  
Explanation: The strings s and t can be made identical by:
- Mapping 'e' to 'a'.
- Mapping 'g' to 'd'.
```

**Example 2:**

```
Input: s = "f11", t = "b23"  
Output: false  
Explanation: The strings s and t can not be made identical as
'1' needs to be mapped to both '2' and '3'.
```

**Example 3:**

```
Input: s = "paper", t = "title"  
Output: true  
```

---

## Constraints

- `1 <= s.length <= 5 * 10⁴`  
- `t.length == s.length`  
- `s` and `t` consist of any valid ASCII character.

---

## Solution Strategy

To solve this problem, I used a **hash map with used-set guard** approach:

1. **Initialize** a `hash_map` (for s→t mappings) and a `used` set (to track already-mapped t characters)
2. **Edge case**: If `len(s) == 1`, return `True`
3. **Iterate** through each index `i`:
   - **If `s[i]` is already mapped**: Check that it maps to `t[i]` — if not, return `False`
   - **If `s[i]` is not mapped**: Check that `t[i]` isn't already used by another mapping — if it is, return `False`. Otherwise, mark `t[i]` as used
   - **Record** the mapping `hash_map[s[i]] = t[i]`
4. **Return** `True` if all characters pass the checks.

### Why This Approach?

The hash map enforces one-to-one mapping from s to t, while the used set prevents two different s characters from mapping to the same t character:
- **Time Complexity:** O(n) — Single pass through both strings
- **Space Complexity:** O(k) — Where k is the number of unique characters (at most 256 for ASCII)

Both constraints are essential for isomorphism: the map ensures consistency (`s[i]` always maps to the same `t[i]`), and the set ensures injectivity (no two characters in `s` share a target in `t`).

---
