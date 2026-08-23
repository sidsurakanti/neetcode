# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def debug(head):
#     curr, res = head, []

#     while curr:
#         res.append(curr.val)
#         curr = curr.next

#     return res

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n, c = 0, head
        while c:
            n += 1
            c = c.next
        # print(n)

        curr = prev = head
        dummy = ListNode(None)
        re = dummy

        for c in range(0, n//k):
            i = 0

            while i < k - 1 and curr.next:
                i += 1
                # reverse
                swap = curr.next
                tmp = swap.next

                swap.next = prev
                curr.next = tmp

                prev = swap
            else:
                re.next = prev # new head of curr group 3*-2-1-
                re = curr # end of curr group 3-2-1*-
                # print(debug(re))
                # print(prev.val, curr.val)
                prev = curr.next # now points to head of next group 3-4*-5-6
                curr = prev # 3-4*
    
        return dummy.next
