# 700. Search in a Binary Search Tree

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/search-in-a-binary-search-tree/description/)

---

## Problem Description

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

---

## Examples

**Example 1:**

![Search BST Example 1](https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg)

```
Input: root = [4,2,7,1,3], val = 2  
Output: [2,1,3]
```

**Example 2:**

![Search BST Example 2](https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg)

```
Input: root = [4,2,7,1,3], val = 5  
Output: []
```

---

## Constraints

- The number of nodes in the tree is in the range `[1, 5000]`.  
- `1 <= Node.val <= 10^7`  
- `root` is a binary search tree.  
- `1 <= val <= 10^7`

---

## Solution Strategy

To solve this problem, I used a **recursive BST search** approach:

1. **Base case**: If `root` is `None`, return `None` (value not found)
2. **Found**: If `root.val == val`, return `root` (the subtree rooted at this node)
3. **Go left**: If `root.val > val`, search the left subtree
4. **Go right**: Otherwise, search the right subtree

### Why This Approach?

Leveraging the BST property makes search highly efficient:
- **Time Complexity:** O(h) - Where h is the tree height (O(log n) for balanced BSTs)
- **Space Complexity:** O(h) - Recursion stack depth

The BST property guarantees that all values in the left subtree are smaller and all values in the right subtree are larger. This allows us to eliminate half the tree at each step, similar to binary search on arrays.

---
