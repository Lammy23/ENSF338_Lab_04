## Implementation of Linked Lists

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
def newNode(x):

    temp = Node(0)
    temp.data = x
    temp.next = None
    return temp

## Binary Search on Linked Lists

def middle(start, last):

    if (start == None):
        return None

    slow = start
    fast = start . next

    while (fast != last):
    
        fast = fast . next
        if (fast != last):
        
            slow = slow . next
            fast = fast . next
        
    return slow

def binarySearchLinked(head,value):

    start = head
    last = None

    while True :
    
        mid = middle(start, last)

        if (mid == None):
            return None

        if (mid . data == value):
            return mid

        elif (mid . data < value):
            start = mid . next

        else:
            last = mid

        if not (last == None or last != start):
            break
    return None

## Implementation of Array Class

class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.data[index] = value

    def length(self):
        return self.size

    def print(self):
        print(self.data)

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]

## Binary Search in Array Class

def binarySearchArray(arr, value):
    low = 0
    high = arr.length() - 1
    while low <= high:
        mid = (low + high) // 2
        if arr.get(mid) == value:
            return mid
        elif arr.get(mid) < value:
            low = mid + 1
        else:
            high = mid - 1
    return None

## Q3

# The complexity of binary search on linked lists is O(n). 
# Basically, in the worst case, the fast pointer is traversing the entire array, 
# even though it skips every other node. 
# The actual complexity is something like O(n/2) but since we don't care 
# about the $1/2$, we write O(n)


sizes = [i for i in range(1, 20)]

def measureBinaryLinkedPerformance():
    import time
    start = time.time()

    value = 11
    binarySearchLinked(head, value)
    end = time.time()
    return end - start

for size in sizes:
    head = newNode(1)
    last = head
    for i in range(size):
        last.next = newNode(i)
        last = last.next
    print("Binary Linked: ", measureBinaryLinkedPerformance())