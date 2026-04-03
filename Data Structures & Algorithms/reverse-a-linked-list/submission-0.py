# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre, curr, next = None, head, head.next

        while curr:
            next = curr.next
            curr.next = pre

            pre = curr 
            curr = next

        return pre
