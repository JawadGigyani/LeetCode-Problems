# 876. Middle of the Linked List

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/middle-of-the-linked-list/description/)

---

## Problem Description

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the **second middle** node.

---

## Examples

**Example 1:**

![Middle of Linked List Example 1](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg)

```
Input: head = [1,2,3,4,5]  
Output: [3,4,5]  
Explanation: The middle node of the list is node 3.
```

**Example 2:**

![Middle of Linked List Example 2](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg)

```
Input: head = [1,2,3,4,5,6]  
Output: [4,5,6]  
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```

---

## Constraints

- The number of nodes in the list is in the range `[1, 100]`.  
- `1 <= Node.val <= 100`

---

## Solution Strategy

To solve this problem, I used the **slow and fast pointer (tortoise and hare)** approach:

1. **Initialize** both `slow` and `fast` pointers at `head`
2. **Loop while `fast` and `fast.next` exist**:
   - Move `slow` one step: `slow = slow.next`
   - Move `fast` two steps: `fast = fast.next.next`
3. **Return** `slow` — when fast reaches the end, slow is at the middle.

### Why This Approach?

The two-pointer technique finds the middle in a single pass:
- **Time Complexity:** O(n) - We traverse the list once
- **Space Complexity:** O(1) - Only using two pointer variables

Since `fast` moves at twice the speed of `slow`, when `fast` reaches the end, `slow` is exactly at the midpoint. For even-length lists, this naturally lands on the second middle node as required.

---
