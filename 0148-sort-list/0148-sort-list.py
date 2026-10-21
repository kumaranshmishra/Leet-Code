# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        res = []
        node = head
        while node:
            res.append(node.val)
            node  = node.next
        res.sort()
        node  = head
        i = 0
        while node:
            node.val = res[i]
            node = node.next
            i+=1
        return head       
        
        