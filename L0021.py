class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            if l1 is None and l2 is None:
                return None
            elif l1 is None:
                result = ListNode(l2.val)
                l2 = l2.next
            else:
                result = ListNode(l1.val)
                l1 = l1.next
        else:
            if l1.val >= l2.val:
                result = ListNode(l2.val)
                l2 = l2.next
            else:
                result = ListNode(l1.val)
                l1 = l1.next
        ans = result
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                result.next = ListNode(l1.val)
                l1, result = l1.next, result.next
            else:
                result.next = ListNode(l2.val)
                l2, result = l2.next, result.next
        if l1 is None:
            while l2 is not None:
                result.next = ListNode(l2.val)
                l2, result = l2.next, result.next
        else:
            while l1 is not None:
                result.next = ListNode(l1.val)
                l1, result = l1.next, result.next
        return ans

A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(3)
B = ListNode(1)
B.next = ListNode(1)
B.next.next =ListNode(4)
sl = Solution()
ans = sl.mergeTwoLists(None,None)
while ans is not None:
    print(ans.val)
    ans = ans.next



