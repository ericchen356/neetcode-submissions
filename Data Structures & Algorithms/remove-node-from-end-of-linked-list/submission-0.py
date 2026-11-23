# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0 

        dummy = ListNode(0, self.reverse(head))
        prev = dummy
        curr = dummy.next

        while count < n-1:
            prev = curr 
            curr = curr.next
            count += 1
        
        prev.next = curr.next

        return self.reverse(dummy.next) 

    def reverse(self, head): 
        prev = None 
        curr = head

        while curr: 
            temp = curr.next 
            curr.next = prev 

            prev = curr
            curr = temp 

        return prev 

