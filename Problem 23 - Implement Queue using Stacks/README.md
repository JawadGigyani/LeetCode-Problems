# 232. Implement Queue using Stacks

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/implement-queue-using-stacks/description/)

---

## Problem Description

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

- `void push(int x)` Pushes element `x` to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

**Note:** You must use only standard operations of a stack (push to top, peek/pop from top, size, and is empty).

---

## Examples

**Example 1:**

```
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2]
myQueue.peek();  // return 1
myQueue.pop();   // return 1, queue is [2]
myQueue.empty(); // return false
```

---

## Constraints

- `1 <= x <= 9`  
- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.  
- All the calls to `pop` and `peek` are valid.

---

## Solution Strategy

To solve this problem, I used a **two-stack reversal** approach:

1. **Maintain two stacks**: `in_stack` (for pushing) and `out_stack` (for reversing order)
2. **Push operation**:
   - Simply append to `in_stack`
3. **Pop operation**:
   - Transfer all elements from `in_stack` to `out_stack` (reversing order)
   - Pop the top of `out_stack` (this is the front of the queue)
   - Transfer everything back to `in_stack`
   - Return the popped value
4. **Peek operation**:
   - Same transfer process as pop, but read `out_stack[-1]` without removing
   - Transfer everything back to `in_stack`
5. **Empty operation**:
   - Check if `in_stack` is empty

### Why This Approach?

Two stacks can simulate a queue by reversing element order:
- **Time Complexity:** O(n) for pop/peek (transferring elements), O(1) for push/empty
- **Space Complexity:** O(n) - Storing all elements across the two stacks

The key insight is that reversing a stack flips the order from LIFO to FIFO. By moving elements from `in_stack` to `out_stack`, the bottom element (first pushed) becomes the top element (first to pop).

---
