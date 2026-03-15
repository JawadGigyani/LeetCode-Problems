# 701. Insert into a Binary Search Tree

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/insert-into-a-binary-search-tree/description/)

---

## Problem Description

You are given the `root` node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

---

## Examples

**Example 1:**

![Insert BST Example 1](https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg)

```
Input: root = [4,2,7,1,3], val = 5  
Output: [4,2,7,1,3,5]  
Explanation: Another accepted tree is:
```

![Insert BST Example 1 Alternative](https://assets.leetcode.com/uploads/2020/10/05/bst.jpg)

**Example 2:**

```
Input: root = [40,20,60,10,30,50,70], val = 25  
Output: [40,20,60,10,30,50,70,null,null,25]
```

**Example 3:**

```
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5  
Output: [4,2,7,1,3,5]
```

---

## Constraints

- The number of nodes in the tree will be in the range `[0, 10^4]`.  
- `-10^8 <= Node.val <= 10^8`  
- All the values `Node.val` are **unique**.  
- `-10^8 <= val <= 10^8`  
- It's guaranteed that `val` does not exist in the original BST.

---

## Solution Strategy

To solve this problem, I used a **recursive BST traversal** approach:

1. **Base case**: If `root` is `None`, we have found the correct empty spot. Create and return a new `TreeNode(val)`.
2. **Go right**: If `val > root.val`, recursively call the function on the right child: `root.right = self.insertIntoBST(root.right, val)`
3. **Go left**: Otherwise (if `val < root.val`), recursively call the function on the left child: `root.left = self.insertIntoBST(root.left, val)`
4. **Return** the current `root` node.

### Why This Approach?

Recursively traversing the BST is both clean and efficient for insertion:
- **Time Complexity:** O(h) - Where h is the tree height (O(log n) for balanced BSTs, O(n) for skewed)
- **Space Complexity:** O(h) - Recursion stack depth

By leveraging the BST property, we eliminate half the tree at each step to find the optimal leaf position. Updating the child pointers during the recursive unwinding safely attaches the new node and naturally maintains all existing structural links.

---
