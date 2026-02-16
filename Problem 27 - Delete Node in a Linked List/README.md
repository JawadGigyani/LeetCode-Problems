# 237. Delete Node in a Linked List

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/delete-node-in-a-linked-list/description/)

---

## Problem Description

There is a singly-linked list `head` and we want to delete a node `node` in it.

You are given the node to be deleted `node`. You will **not** be given access to the first node of `head`.

All the values of the linked list are unique, and it is guaranteed that the given node `node` is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

- The value of the given node should not exist in the linked list.
- The number of nodes in the linked list should decrease by one.
- All the values before `node` should be in the same order.
- All the values after `node` should be in the same order.

---

## Examples

**Example 1:**

![Delete Node Example 1](https://assets.leetcode.com/uploads/2020/09/01/node1.jpg)

```
Input: head = [4,5,1,9], node = 5  
Output: [4,1,9]  
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
```

**Example 2:**

![Delete Node Example 2](https://assets.leetcode.com/uploads/2020/09/01/node2.jpg)

```
Input: head = [4,5,1,9], node = 1  
Output: [4,5,9]  
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
```

---

## Constraints

- The number of the nodes in the given list is in the range `[2, 1000]`.  
- `-1000 <= Node.val <= 1000`  
- The value of each node in the list is unique.  
- The `node` to be deleted is in the list and is not a tail node.

---

## Solution Strategy

To solve this problem, I used a **value copy and pointer skip** approach:

1. **Copy the next node's value** into the current node: `node.val = node.next.val`
2. **Skip the next node** by updating the pointer: `node.next = node.next.next`

### Why This Approach?

Since we don't have access to the previous node, we can't do a traditional deletion. Instead, we effectively "become" the next node:
- **Time Complexity:** O(1) - Only two operations
- **Space Complexity:** O(1) - No extra space needed

The trick is that instead of removing the current node (which requires access to the previous node), we overwrite the current node's value with the next node's value and then remove the next node. This achieves the same result as deleting the given node.

---
