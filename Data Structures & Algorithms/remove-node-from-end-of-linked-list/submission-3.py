# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # step 1: offset guide pointer by n
        guide = head
        i = n
        while guide.next and i > 0:
            guide = guide.next
            i -= 1

        # this would mean n == len of list
        # since guide can only go up to len - 1
        # meaning we have to remove the head node
        if i > 0: 
            return head.next

        # step 2: 
        # while guide reaches end of list
        # curr will be n steps behind 
        # therefore landing at index_{len - n}
        curr = head
        while guide.next:
            curr = curr.next
            guide = guide.next
        curr.next = curr.next.next

        return head
        


