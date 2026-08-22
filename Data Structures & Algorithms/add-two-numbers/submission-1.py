# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        i = l1
        j = l2

        # add into i
        # if there's leftovers in j: i.next = j.next at the end
        carry = 0
        prev = None
        while i and j:
            s = i.val + j.val + carry
            # print(s)
            i.val = s % 10
            carry = s // 10

            prev = i
            i, j = i.next, j.next

        # 1) i still has digits
        # OR
        # 2) j still has digits
        # AND
        # 3) leftover carry

        if j:
            prev.next = j

        # case 0:
        # 2 (carry: 0) -> 9 -> n ANS: do nothing

        # case 1:
        # 0 (c=1) -> 1 - n
        # case 2: 
        # 2 (c=1) -> n
        # case 3:
        # 0 (c=1) -> 9 -> 8 -> n 
        # case 4:
        # 0 (c=1) -> 9 -> 9 -> n 

        if carry:
            i = prev.next
            while i: # if leftover nodes
                s = i.val + carry
                i.val = s % 10
                carry = s // 10

                prev = i
                i = i.next
            if carry:
                prev.next = ListNode(carry)

        return l1