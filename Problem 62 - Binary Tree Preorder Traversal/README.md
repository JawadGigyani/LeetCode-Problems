# 144. Binary Tree Preorder Traversal

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)

---

## Problem Description

Given the `root` of a binary tree, return the preorder traversal of its nodes' values.

---

## Examples

**Example 1:**

![Preorder Traversal Example 1](https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png)

```
Input: root = [1,null,2,3]  
Output: [1,2,3]
```

**Example 2:**

![Preorder Traversal Example 2](https://assets.leetcode.com/uploads/2024/08/29/tree_2.png)

```
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]  
Output: [1,2,4,5,6,7,3,8,9]
```

**Example 3:**

```
Input: root = []  
Output: []
```

**Example 4:**

```
Input: root = [1]  
Output: [1]
```

---

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.  
- `-100 <= Node.val <= 100`

---

## Solution Strategy

To solve this problem, I used a **recursive DFS** approach:

1. **Initialize** an empty `stack` list (used as the result)
2. **Define a recursive `traverse(node)` function**:
   - Base case: if `node` is `None`, return
   - **Append** the current node's value (Root first)
   - **Recurse** on the left subtree
   - **Recurse** on the right subtree
3. **Call** `traverse(root)` and **return** `stack`.

### Why This Approach?

Recursive preorder traversal naturally follows the Root → Left → Right pattern:
- **Time Complexity:** O(n) - We visit every node exactly once
- **Space Complexity:** O(n) - Result list stores n values, plus O(h) recursion stack

Preorder traversal processes the current node **before** its children, making it useful for creating copies of trees or prefix expressions.

---
