# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head # 4

        while curr.next: # 4-5-6-null | 5-4-6-n
            tmp = curr.next # -5-6-null | -6-n
            curr.next = tmp.next # 4-6-null | -4-n

            tmp.next = head # 5-4-6-null | -6-5-4-n
            head = tmp # 5-4-6-n | 6-5-4-n

        return head






        