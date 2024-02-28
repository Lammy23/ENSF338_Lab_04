## Arrays

### Advantages
* Access to elements using index is $O(1)$
* Memory locality leads to better cache performance.

### Disadvantages
* Insertions and deletions in the middle of the array are $O(n)$ because the right side needs to be shifted.
* The size of an array is fixed when declared and will have to be redeclared to fit more elements than the current capacity.

## Linked Lists

### Advantages
* Insertion and deletion are $O(1)$ at the head (and tail for lists with tail pointers)
* No pre-allocated memory so the list size can grow.

### Disadvantages
* Accessing middle elements requires traversing the array whichi is $O(n)$

## Implementing Replace

The trick to implementing replace in an array is simple. A replace is usually a deletion followed by an insertion. But both those operations are $O(n)$. This mitigate this, we could simply mark the address where the replacement element should go and overwrite the element at that memory location.

## Sort Feasibility on Doubly Linked List

### Insertion sort
This sorting technique is feasible because with the 'prev' pointers, we can use the algorithm to compare an element in the unsorted area to elements in the sorted area and figure out where it needs to go.

### Merge sort
This sorting technique is feasible because we can recursively call merge sort on either half of the linked list and then mergin them.

## Complexity Analysis

### Insertion sort
* Array: $O(n^2)$ complexity due to repeated traversal and shifting.
* Doubly Linked List: $O(n^2)$ time complexity due to traversal and insertion.

### Merge Sort
* Array: $O(n \log{n})$ time complexity due to the divide-and-conquer approach.
* Doubly Linked List: $O(n \log{n})$ time complexity due to efficient splitting and merging.