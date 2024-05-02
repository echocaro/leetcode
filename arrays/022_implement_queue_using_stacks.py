"""
Implement a first in first out (FIFO) queue using only two
stacks. The implemented queue should support all the functions
of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and
returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false
otherwise.
Notes:

You must use only standard operations of a stack, which means
only push to top, peek/pop from top, size, and is empty
operations are valid.
Depending on your language, the stack may not be supported
natively. You may simulate a stack using a list or deque
(double-ended queue) as long as you use only a stack's standard
operations.

Note:
when we append the 'x' to stack1, it will follow the principle
in the sense that items get added to the end of the list

but when we go to perform a pop, we need to reverse this list
as doing pop(0) is inefficient.
"""


class MyQueue(object):
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
