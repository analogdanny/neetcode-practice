# Reverse Linked List
#
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
#
# Example 1:
#   Input: head = [0,1,2,3]
#   Output: [3,2,1,0]
#
# Example 2:
#   Input: head = []
#   Output: []
#
# Constraints:
#     0 <= The length of the list <= 1000.
#     -1000 <= Node.val <= 1000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # My attempt, honestly not bad.
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        curr = head

        # We will create a new list
        while curr:
            # create the list node
            new_node = ListNode(curr.val)

            # if this is not the head value, we align pointers
            if prev:
                new_node.next = prev

            # set the prev node to the new node for connecting
            prev = new_node
            curr = curr.next

        # When the above loop ends, we will have prev == the new head for the 
        # linked list and curr will be None from the tail pointing to None
        return prev 

    # Optimal solution without use of creating new nodes.
    # def reverseList(self, head: ListNode) -> ListNode:
    # prev, curr = None, head

    # while curr:
    #     temp = curr.next
    #     curr.next = prev
    #     prev = curr
    #     curr = temp
    # return prev