# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return None
        start = head
        result = []
        for i in range(n+1):
            result.append(0)
        while head is not None:
            result.remove(result[0])
            result.append(head)
            head = head.next
        result.append(None)
        if result[0] == 0:
            return start.next
        else:
            result[0].next = result[2]
            return start