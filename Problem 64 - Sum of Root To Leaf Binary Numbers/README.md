# 1022. Sum of Root To Leaf Binary Numbers

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/)

---

## Problem Description

You are given the `root` of a binary tree where each node has a value `0` or `1`. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is `0 -> 1 -> 1 -> 0 -> 1`, then this could represent `01101` in binary, which is `13`.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the **sum of these numbers**.

The test cases are generated so that the answer fits in a **32-bits** integer.

---

## Examples

**Example 1:**

![Sum of Root To Leaf Binary Numbers Example 1](https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png)

```
Input: root = [1,0,1,0,1,0,1]  
Output: 22  
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
```

**Example 2:**

```
Input: root = [0]  
Output: 0
```

---

## Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.  
- `Node.val` is `0` or `1`.

---

## Solution Strategy

To solve this problem, I used a **recursive DFS string concatenation** approach:

1. **Initialize** an empty list `self.result` to store binary strings
2. **Define a recursive `dfs(node, path)`**:
   - If `node` is `None`, return
   - **Append** the current node's value to the binary string `path` (`path += str(node.val)`)
   - **Leaf check**: If the node is a leaf, append the full `path` to `self.result`
   - **Recurse** on left and right children
3. **Run** `dfs(root, "")`
4. **Sum the values**: Iterate through `self.result`, convert each binary string to an integer using `int(i, 2)`, and accumulate the sum.
5. **Return** the total sum.

### Why This Approach?

DFS cleanly extracts all root-to-leaf paths as strings:
- **Time Complexity:** O(n * h) - We visit every node, but string concatenation takes O(h) where h is tree height
- **Space Complexity:** O(n * h) - Storing all paths as strings, plus recursion stack

By converting the path to a binary string as we descend, parsing it into a base-10 integer at the end using `int(string, 2)` becomes extremely simple and readable.

---
