# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
            
        
        curr = head.next
        prev = head
        
        while curr != None:
            # curr is gonna get swapped to start of list
            # prev shud always point to the curr after it gets swapped
            # temp is the pointers that we need to save while swapping
            # head = original start of list, this needs to point to stuff we haven't swapped yet
            temp = curr.next # save pointers for 2, 3

            # curr = 1; head, prev = 0; temp = 2, 3
            curr.next = prev # 1 -> 0
            head.next = temp # from 0 -> 1 to 0 -> 2, 3, 0 ->

            prev = curr # new start = what we js swapped to first
            curr = temp # set curr to 2

        return prev

            




            