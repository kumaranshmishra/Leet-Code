# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        res = []
        node = head
        while node != None:
            res.append(node.val)
            node = node.next
        node = head
        x = len(res)
        while node != None:
            node.val = res[x-1] 
            x -= 1
            node = node.next

        return head        
        