# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        list1 = []
        node = head
        while node:
            list1.append(node.val)
            node = node.next    
        right = float('-inf')
        res = []
        for i in range(len(list1)-1,-1,-1):
            if list1[i] >= right:
                res.append(list1[i])
                right = list1[i]
        res.reverse()
        dummy  = ListNode(0)
        node = dummy
        for i in res:
            node.next = ListNode(i)
            node = node.next
        return dummy.next           