# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            # remove only node bc guarantted 1 <= n
            return head.next

        # step 1: offset guide pointer by n
        guide = head
        i = n
        while guide.next and i > 0:
            guide = guide.next
            i -= 1
        
        print("guide =", guide.val, "i =", i)

        # step 2: 
        # while guide reaches end of list
        # curr will be n steps behind 
        # therefore landing at index_{len - n}
        curr = head
        print(curr.val)
        while guide.next:
            curr = curr.next
            guide = guide.next

        print(guide.val, curr.val, i)

        # remove curr.next
        if i > 0:
            return curr.next
        curr.next = curr.next.next
        
        
        return head
        


