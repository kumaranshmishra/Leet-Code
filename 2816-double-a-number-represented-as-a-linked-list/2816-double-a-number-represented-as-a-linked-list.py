class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val >= 5:
            head = ListNode(0, head)

        node = head

        while node:
            node.val *= 2

            if node.next and node.next.val >= 5:
                node.val += 1

            node.val %= 10
            node = node.next

        return head