# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

            first = second = head
            while second and second.next is not None:
                first = first.next
                second = second.next.next
            return first
        