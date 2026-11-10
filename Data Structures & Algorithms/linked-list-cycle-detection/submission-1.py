# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        dict = {}

        curr = head 
        
        while curr: 
            if curr in dict: 
                return True
            else: 
                dict[curr] = 1
            curr = curr.next
            
        return False

        