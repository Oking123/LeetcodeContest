# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = head
        while head is not None:
            if head.next is None:
                break
            while True:
                if head.next is None:
                    break
                if head.next.val != head.val:
                    head = head.next
                    break
                else:
                    head.next = head.next.next
        return ans
