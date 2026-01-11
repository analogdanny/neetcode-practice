# Linked Lists
#
# - Made up of list nodes or nodes
# - A list node is an object that encapsulates 2 things at a minimum
#   - value: Can be a simple number or an object
#   - next: pointer


### Basic code for nodes and manual linking

# class Node:
#     def __init__(self, value, next=None):
#         self.value = ""
#         self.next = next

# ListNode1 = Node("Red")
# ListNode2 = Node("Blue")
# ListNode3 = Node("Green")

# ListNode1.next = ListNode2
# ListNode2.next = ListNode3
# ListNode3.next = ListNode1

# # print(ListNode1, ListNode1.next)
# # print(ListNode2, ListNode2.next)
# # print(ListNode3, ListNode3.next)

# # Unset the infinite linked list
# ListNode3.next = None

# # Loop through Linked List
# cur = ListNode1

# while(cur != None):
#     print(f"cur = {cur}, setting to next = {cur.next}")
#     cur = cur.next

# print(f"cur = {cur}, at end of linked list")


### Linked List data structure code

class LinkedList:
        
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        
    # Insert new node into Linked List (singly)
    def append(self, value):
        new_node = self.Node(value)
        
        # If the head isn't set, the first node initializes the list
        if not self.head:
            self.head = new_node
            return
        
        # Otherwise, we continue with searching for the tail node 
        cur = self.head
        
        # When at the tail node, the current nodes next node is null
        while cur.next != None:
            cur = cur.next
        
        # Assign once we have found tail node    
        cur.next = new_node
        
    # Allows the LinkedList object itself to be iterated over (e.g., `for value in linked_list`).
    # __iter__ is a special Python method that returns an iterator.
    # By yielding each node's value one at a time, this class integrates with Python's
    # iteration protocol without exposing internal structure like `head` or `Node`.
    def __iter__(self):
        cur = self.head
        
        while cur:
            # returns one value at a time, pausing the function until the next value is requested
            yield cur.value
            cur = cur.next
                

# Executed code

linked_list = LinkedList()
linked_list.append("Red")
linked_list.append("Blue")
linked_list.append("Green")

print(linked_list)

for value in linked_list:
    print(value)
