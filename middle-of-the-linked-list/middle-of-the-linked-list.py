# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        
        temp = head
        while temp:
            count += 1
            temp = temp.next
        countHalf = count//2
        while countHalf > 0:
            print(countHalf)
            head = head.next
            countHalf -=1
        return head