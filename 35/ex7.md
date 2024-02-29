```
def reverse(self):
    newhead = None
    prevNode = None
    for i in range(self.get_size()-1, -1, -1):
        currNode = self.get_element_at_pos(i)
        currNewNode = Node(currNode.data)
        if newhead is None:
            newhead = currNewNode
        else:
            prevNode.next = currNewNode
        prevNode = currNewNode
    self.head = newhead
```

## Complexity Analysis

Let's step through the code:

1. `newhead = None` is $O(1)$ 
2. `prevNode = None` is $O(1)$

3. `for i in range(self.get_size() - 1, -1, -1):` is $O(n)$. Generally, we can think of it as these two lines merged into one:

```
size = self.get_size()
for i in range(size - 1, -1, -1):
```

Both lines are $O(n)$. So far, we get\
$Total = O(1) + O(1) + O(n) + O(n) = O(n)$

4. Within the for loop, `currNode = self.get_element_at_pos(i)` is $O(n)$ because getting an element in a linked list requires traversing the list which is $O(n)$. 

5. `currNewNode = Node(currNode.data)` is $O(1)$

6. The `if` block has functions that are all $O(1)$

7. `prevNode = currNewNode` is $O(1)$

Thus,\
$Total = O(n) * (O(n) + 3 * O(1)) = O(n^2)$

8. Lastly, `self.head = newhead` is $O(1)$

Thus, the complexity is $O(n^2) + O(1) = O(n^2)$


```
def reverseModified(self):
    currNode = self.head            # Set the current node to the head
    prevNode = None
    nextNode = None
    if not currNode:                # Check if head points to `None`, then there's 
                                    # nothing to do
        return
    while currNode is not None:
        nextNode = currNode.next    # remember the next node
        currNode.next = prevNode    # change 'next' pointer of current node to
                                    # previous node
        prevNode = currNode         # shift previous node forward
        currNode = nextNode         # shift current node forward
    
    self.head = prevNode            # When all is said and done. Assign the new head
```

This implementation reduces the complexity from $O(n^2)$ to $O(n)$. We increase the number of pointers from two to three. This enables us to keep track of both the previous node and the next node from the current node, resulting in the need to traverse the linked list only once.