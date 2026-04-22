# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        l2 = slow.next
        slow.next = None

        prev = None
        curr = l2
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        l2 = prev
            
        l1 = head
        while l2:
            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2
            l2.next = tmp1

            l2 = tmp2
            l1 = tmp1
        
            
        
        