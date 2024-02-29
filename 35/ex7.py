## Testing `reverse`

# Imports

import numpy as np
import matplotlib.pyplot as plt
import timeit
from scipy.optimize import curve_fit

class Node:

    def __init__(self, val, next= None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self, head= None):
        self.head = head

    def addNode(self, val):
        tempNode = Node(val)
        if self.head is None:
            self.head = tempNode
            return

        start = self.head
        while True:
            if start.next is None:
                start.next = tempNode
                break
            start = start.next

    def insert_head(self, node):
        node.next = self.head
        self.head = node
    
    def insert_tail(self, node):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        node.next = None

    def get_size(self):
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def get_element_at_pos(self, pos):
        curr = self.head
        counter = 0
        while counter < pos:
            curr = curr.next
            counter += 1
        return curr
        
    def printList(self):
        curr = self.head
        while curr is not None:
            print(f"{curr.val} -> ", end='')
            curr = curr.next
        print("None")

    # Changed 'data' to 'val'
    def reverseOld(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.val)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    def reverseModified(self):
        currNode = self.head            # Set the current node to the head
        prevNode = None
        nextNode = None
        if not currNode:                # Check if head points to `None`, then there's nothing to do
            return
        while currNode is not None:
            nextNode = currNode.next    # remember the next node
            currNode.next = prevNode    # change 'next' pointer of current node to previous node
            prevNode = currNode         # shift previous node forward
            currNode = nextNode         # shift current node forward
        
        self.head = prevNode            # When all is said and done. Assign the new head

# Assign sizes

sizes = [1000, 2000, 3000, 4000]

def measureOld(size):
    listy = LinkedList()
    for i in range(size):
        listy.addNode(i)
    avg_time = timeit.timeit(stmt= lambda: listy.reverseOld(), number= 100) / 100
    return avg_time

def measureModified(size):
    listy = LinkedList()
    for i in range(size):
        listy.addNode(i)
    avg_time = timeit.timeit(stmt= lambda: listy.reverseModified(), number= 100) / 100
    return avg_time

old = []
for size in sizes:
    old.append(measureOld(size))

modified = []
for size in sizes:
    modified.append(measureModified(size))

## Curve fitting

def nSquaredModel(x, a, b):
    return a * (x ** 2) + b

def linearModel(x, a, b):
    return a * x + b

p_old, _ = curve_fit(nSquaredModel, sizes, old)
p_modified, _ = curve_fit(linearModel, sizes, modified)

## Plotting

fig, ax = plt.subplots(nrows= 1, ncols= 1, figsize= (5, 5))

ax.scatter(sizes, old, label= 'old', color= 'red')
ax.plot(sizes, nSquaredModel(np.array(sizes), *p_old), label= 'old curve', color= 'red')

ax.scatter(sizes, modified, label= 'modified', color= 'blue')
ax.plot(sizes, linearModel(np.array(sizes), *p_modified), label= 'modified curve', color= 'blue')

ax.set_xlabel("Array Sizes")
ax.set_ylabel("Average Time")

ax.legend()

plt.tight_layout()
plt.show()