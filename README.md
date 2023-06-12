# Data Structures and Algorithms in Python
## Search Algorithms
**Linear Search:**

Time complexity - O(n)

The linear search algorithm is used to find the index location
of a key by visiting each item in a collection until the key 
is found or the end of the collection is reached.

**Binary Search:**

Time complexity - O(log(n))

The binary search algorithm is used to find the index location
of a key using a binary strategy. The middle element of a sorted
collection is compared against the key, either returning the index
location if matched or repeating the process using higher or lower
information to eliminate half of the remaining collection. This
strategy is repeated until the key is found or the end of the
collection is reached.
___
## Sorting Algorithms
**Selection Sort**

Time complexity - O(n^2)

The selection sort algorithm uses nested for loops to 
sequentially iterate through an unordered collection. Each inner
pass is used to find the index of the smallest item. 
At the conclusion of each inner pass the smallest item is swapped
in to the index of the outer loop.

**Insertion Sort**

Time complexity - O(n^2)

Insertion sort progresses through an unordered container and
walks back lower elements to their proper index. An outer for loop
keeps track of the start index for each round of walk backs 
performed by the inner while loop. 

**Shell Sort**

Time complexity - O(n^2)

Shell sort utilizes the insertion sort strategy but makes
use of a gaping technique to reduce the overall comparisons.
The gap values specified should start at half the containers size,
decrease in a log2 manner, always end in 1. 
EX: `[8, 4, 2, 1]`

**Quick Sort**

Time complexity - O(n^2), AVG: O(nlogn)

Quick sort recursively partitions the unordered container
sorting each diminishing segment as it goes. The partitions are
split by determining a middle pivot index at the center of each
sub-container and simultaneously iterating from the start and end
of the list to compare and swap values such that at the end of
each round, the lower values are to the left and higher values
to the right of the pivot.

**Merge Sort**

Time complexity - O(nlogn)

Merge sort divides the unordered container and its subsequent 
sub-containers into halves recursively sorting them before merging
them back in sorted order.

**Radix Sort**

Time complexity - O(nk)

Radix sort uses buckets to separate an unordered container of
integers by significant digit. Beginning with the ones column
Radix sort moves up in digits until the most significant digit
of the longest number has been processed.

**Heap Sort**

Time complexity - O(nlogn)

With each pass of heapsort over an unordered container it will 
remove the largest element and store it at the end of the container
in sorted order. This is achieved by replacing the root element
(largest) with the last element and then re-heapify the 
container using a percolate down method.
___
## Abstract Data Types
**Singly linked list**

A node based list where each node references the next node in
the list. Methods include: append, prepend, insert_after,
remove_after, and traverse.

**Doubly linked list**

A node based list where each node references the next and previous
nodes in the list. Methods include: append, prepend, insert_after,
remove, traverse, reverse_traverse.

**Array**

A dynamically allocated container for storing elements. The array
will allocate container size (up or down) automatically depending
on the number of elements in the container. This ADT had the
methods: append, insert, remove, and search.

**Stack**

Utilizes Python's list to create a lifo container. Includes 
methods peek, pop and push.

**Queue**

Utilizes Python's list to create a fifo container. Includes
methods dequeue, enqueue, and peek.

**Hash table**

This implementation uses open addressing with a linear probing
approach to map key/value pairs to a given index. The hashing
scheme uses Python's build in hash function modulo size of the
array to map buckets to index numbers.
___
## Tree Structures
**Binary Search Tree**

A basic tree with an ordering property such that left child < node
< right child. This implementation has insert, remove, and
search methods.

**AVL Tree**

An AVL Tree is a balanced BST which to maintain search efficiency.
The tree uses a node rotation scheme to dynamically balance as
nodes are inserted or removed. Methods include insert, remove key,
and search.

**Red Black Tree**

A red black tree is a BST where we have two node types. With the
two node types combined with standard BST rules we can devise a
scheme to keep the tree as balanced as possible resulting in low
insert, remove and search times. Methods include insert, remove key
and search.

**Max Heap**

A max heap is a complete tree that maintains the single property
of a nodes children's keys are always equal or less than the nodes
key. This results in the root of the tree having the greatest key.
This implementation uses a binary tree with the methods insert and
remove.


