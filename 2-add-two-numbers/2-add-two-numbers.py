# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode()
        tmp = ans
        
        carry = 0
        while l1 or l2:
            if l1:
                x = l1.val
            else:
                x = 0
            
            if l2:
                y = l2.val
            else:
                y = 0
            
            sum = carry + x + y
            carry = sum // 10
            tmp.next = ListNode(sum % 10)
            tmp = tmp.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            tmp.next = ListNode(carry)
        
        return ans.next