# 142. Linked List Cycle II

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/linked-list-cycle-ii/description/)

---

## Problem Description

Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

**Do not modify the linked list.**

---

## Examples

**Example 1:**

![Linked List Cycle Example 1](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```
Input: head = [3,2,0,-4], pos = 1  
Output: tail connects to node index 1  
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

**Example 2:**

![Linked List Cycle Example 2](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

```
Input: head = [1,2], pos = 0  
Output: tail connects to node index 0  
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

**Example 3:**

![Linked List Cycle Example 3](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

```
Input: head = [1], pos = -1  
Output: no cycle  
Explanation: There is no cycle in the linked list.
```

---

## Constraints

- The number of the nodes in the list is in the range `[0, 10^4]`.  
- `-10^5 <= Node.val <= 10^5`  
- `pos` is `-1` or a valid index in the linked list.

---

## Solution Strategy

To solve this problem, I used **Floyd's Cycle Detection algorithm** (tortoise and hare) with a two-phase approach:

1. **Phase 1 — Detect the cycle**:
   - Initialize `slow = fast = head`
   - Move `slow` one step and `fast` two steps
   - If they meet, a cycle exists
2. **Phase 2 — Find the cycle start**:
   - Reset `slow` to `head`
   - Move both `slow` and `fast` one step at a time
   - The node where they meet is the **cycle start**
3. If `fast` reaches `None`, return `None` (no cycle).

### Why This Approach?

Floyd's algorithm mathematically guarantees finding the cycle start:
- **Time Complexity:** O(n) - Both phases traverse the list linearly
- **Space Complexity:** O(1) - Only using two pointer variables

The math behind Phase 2: if the distance from head to cycle start is `a`, and the meeting point is `b` steps into the cycle, then resetting one pointer to head and moving both at the same speed will cause them to meet exactly at the cycle start after `a` steps.

---
