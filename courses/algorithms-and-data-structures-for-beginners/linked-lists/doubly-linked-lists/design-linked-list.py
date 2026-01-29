# 707. Design Linked List
# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and 
# next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in 
# the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:
# - MyLinkedList() Initializes the MyLinkedList object.
# - int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# - void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, 
# the new node will be the first node of the linked list.
# - void addAtTail(int val) Append a node of value val as the last element of the linked list.
# - void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index 
# equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater 
# than the length, the node will not be inserted.
# - void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

# Example 1:

#     Input
#         ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
#         [[], [1], [3], [1, 2], [1], [1], [1]]
#     Output
#         [null, null, null, null, 2, null, 3]

#     Explanation
#         MyLinkedList myLinkedList = new MyLinkedList();
#         myLinkedList.addAtHead(1);
#         myLinkedList.addAtTail(3);
#         myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
#         myLinkedList.get(1);              // return 2
#         myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
#         myLinkedList.get(1);              // return 3

# Constraints:
#     0 <= index, val <= 1000
#     Please do not use the built-in LinkedList library.
#     At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.




class ListNode(object):

    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList(object):

    # MyLinkedList() Initializes the MyLinkedList object.
    def __init__(self):
        self.head = None
        self.tail = None

    # int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        temp = self.head
        i = 0
        
        while temp:
            if i == index:
                return temp.val
            
            temp = temp.next
            i += 1

        return -1
        
    # void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, 
    # the new node will be the first node of the linked list.
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        # Create a node that points to the current heads and nothing as a previous pointer
        # Note: should this point to tail?
        node = ListNode(val, None, self.head)
        
        if self.head:
            self.head.prev = node
        
        self.head = node
        # print("addAtHead: Adding new head: " + str(self.head.val))
        # print("addAtHead: node = " + str(node))
        # print("addAtHead: node prev = " + str(node.prev) + " and next = " + str(node.next))
        # print("addAtHead: head prev = " + str(self.head.prev) + " and next = " + str(self.head.next))

        if not self.tail:
            self.tail = self.head
            # print("addAtHead: Tail was None, assigning to head: " + str(self.tail.val))
        
    # void addAtTail(int val) Append a node of value val as the last element of the linked list.
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = ListNode(val, self.tail, None)
        
        if self.tail:
            self.tail.next = node
        
        self.tail = node
        # print("addAtTail: Adding new tail: " + str(self.tail.val))
        # print("addAtHead: node = " + str(node))
        # print("addAtHead: node prev = " + str(node.prev) + " and next = " + str(node.next))
        # print("addAtHead: tail prev = " + str(self.tail.prev) + " and next = " + str(self.tail.next))

        if not self.head:
            self.head = self.tail
            # print("addAtTail: Head was None, assigning to tail: " + str(self.head.val))

    # void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index 
    # equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater 
    # than the length, the node will not be inserted.
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # print("addAtIndex: Adding index, val pair = ", str(index), str(val))

        if index == 0:
            # print("addAtIndex: Calling addAtHead with val = ", str(val))
            self.addAtHead(val)
            return

        temp = self.head
        i = 0

        while temp:
            # print("addAtIndex: temp.val = ", str(temp.val))
            if i == index:
                # add before indexth node
                node = ListNode(val, temp.prev, temp)
                temp.prev.next = node
                temp.prev = node
                # print("addAtIndex: Found index. i = ", str(i))
                return

            temp = temp.next
            i += 1
            # print("addAtIndex: temp assinged to next listnode, i = ", str(i))

        # if index is the length of the linked list, add to the end
        if i == index:
            # print("addAtIndex: Calling addAtTail with val = ", str(val))
            self.addAtTail(val)
            return
    

    # void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        # might need to handle head and tail separately.


        temp = self.head
        i = 0

        while temp:
            if i == index:
                # Delete the indexth node in the linked list
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                
                if temp == self.head:
                    self.head = temp.next
                elif temp == self.tail:
                    self.tail = temp.prev
                
                return

            temp = temp.next
            i += 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)