# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        ans = result

        while l1 is not None and l2 is not None:
            result.val += l1.val+l2.val
            if result.val >= 10:
                result.val -= 10
                result.next = ListNode(1)
            elif l1.next is None and l2.next is None:
                result.next = None
            else:
                result.next = ListNode(0)
            result, l1, l2 = result.next, l1.next, l2.next
        while l1 is not None:
            result.val += l1.val
            if result.val >= 10:
                result.val -= 10
                result.next = ListNode(1)
            elif l1.next is not None:
                result.next = ListNode(0)
            result, l1= result.next, l1.next
        while l2 is not None:
            result.val += l2.val
            if result.val >= 10:
                result.val -= 10
                result.next = ListNode(1)
            elif l2.next is not None:
                result.next = ListNode(0)
            result, l2 = result.next, l2.next
        return ans


