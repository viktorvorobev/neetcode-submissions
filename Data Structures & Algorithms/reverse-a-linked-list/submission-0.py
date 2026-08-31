# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next_node = None
        current_node = head
        while current_node:
            temp = current_node.next  # store next node
            current_node.next = next_node  # reverse the link
            next_node = current_node
            current_node = temp  # move to next node
        return next_node