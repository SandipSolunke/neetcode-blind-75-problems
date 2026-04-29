# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            ans = ListNode(list1.val)
            list1 = list1.next
        else:
            ans = ListNode(list2.val)
            list2 = list2.next
            
        ans_head = ans

        while list1 or list2:
            if not list1:
                ans.next = list2
                list2 = list2.next
            elif not list2:
                ans.next = list1
                list1 = list1.next

            elif list1.val < list2.val:
                ans.next = list1
                list1 = list1.next
            else:
                ans.next = list2
                list2 = list2.next

            ans = ans.next
        
        return ans_head 