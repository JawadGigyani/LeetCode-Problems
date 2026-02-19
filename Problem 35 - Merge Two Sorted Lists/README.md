# 21. Merge Two Sorted Lists

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/merge-two-sorted-lists/description/)

---

## Problem Description

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

---

## Examples

**Example 1:**

![Merge Two Sorted Lists](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```
Input: list1 = [1,2,4], list2 = [1,3,4]  
Output: [1,1,2,3,4,4]
```

**Example 2:**

```
Input: list1 = [], list2 = []  
Output: []
```

**Example 3:**

```
Input: list1 = [], list2 = [0]  
Output: [0]
```

---

## Constraints

- The number of nodes in both lists is in the range `[0, 50]`.  
- `-100 <= Node.val <= 100`  
- Both `list1` and `list2` are sorted in non-decreasing order.

---

## Solution Strategy

To solve this problem, I used a **dummy node with iterative merging** approach:

1. **Handle edge cases**: If both lists are empty, return `None`. If one is empty, return the other.
2. **Create a dummy node** and a pointer `new_list` to build the merged list.
3. **Loop while both lists have nodes**:
   - Compare `list1.val` and `list2.val`
   - Attach the smaller node to `new_list.next` and advance that list's pointer
   - Move `new_list` forward
4. **Attach the remaining nodes** from whichever list is not exhausted.
5. **Return** `dummy.next` — the head of the merged list.

### Why This Approach?

The dummy node simplifies edge case handling for the merged list's head:
- **Time Complexity:** O(n + m) - Where n and m are the lengths of the two lists
- **Space Complexity:** O(1) - We reuse existing nodes, only creating the dummy node

By comparing and linking nodes one at a time, we build the merged list in sorted order without allocating new nodes.

---
