class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2



A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(3)
B = ListNode(1)
B.next = ListNode(1)
B.next.next =ListNode(4)
sl = Solution()
ans = sl.mergeTwoLists(A, B)
while ans is not None:
    print(ans.val)
    ans = ans.next



