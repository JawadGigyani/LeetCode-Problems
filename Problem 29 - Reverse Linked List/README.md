# 206. Reverse Linked List

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/reverse-linked-list/description/)

---

## Problem Description

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

---

## Examples

**Example 1:**

![Reverse Linked List Example 1](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

```
Input: head = [1,2,3,4,5]  
Output: [5,4,3,2,1]
```

**Example 2:**

![Reverse Linked List Example 2](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

```
Input: head = [1,2]  
Output: [2,1]
```

**Example 3:**

```
Input: head = []  
Output: []
```

---

## Constraints

- The number of nodes in the list is the range `[0, 5000]`.  
- `-5000 <= Node.val <= 5000`

---

## Solution Strategy

To solve this problem, I used an **iterative pointer reversal** approach:

1. **Initialize**: `curr = head` and `prev = None`
2. **Loop while `curr` is not None**:
   - Save the next node: `temp = curr.next`
   - Reverse the pointer: `curr.next = prev`
   - Move `prev` forward: `prev = curr`
   - Move `curr` forward: `curr = temp`
3. **Return** `prev` — the new head of the reversed list.

### Why This Approach?

Iterative reversal is the most efficient way to reverse a linked list:
- **Time Complexity:** O(n) - We traverse the list once
- **Space Complexity:** O(1) - Only using three pointer variables

At each step, we reverse one link by pointing the current node back to the previous node. The `temp` variable saves the next node before we overwrite the pointer, ensuring we don't lose the rest of the list.

---
