# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        if length == 1 and n == 1:
            return None
        i = 1
        point = head
        while i < length - n:
            head = head.next
            i += 1
        if length - n <= 1:
            if length - n == 0:
                return point.next
            point.next = point.next.next
            return point
        next = head.next.next
        head.next = None
        head.next = next
        return point
        
        '''
        x = self.reverse(head) #reverse list, remove nth element, reverse again, return
        curr = x
        y = n
        while n > 0:
            curr = curr.next
            n -= 1
        print(curr)
        
        while y > 2:
            
            y -= 1
        
        return self.reverse(x)
    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
    '''