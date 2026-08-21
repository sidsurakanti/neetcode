# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1: split into two lists
            # 1st list upto middle node # 0, 1, 2, 3
            # 2nd list the rest and reverse # 6, 5, 4
        # step 2: merge them
        
        # step 1:
        # can use a slow and fast pointer
        # to get to end of list and start of list
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow

        # reverse second part of list
        curr = second
        while curr.next:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = second
            second = tmp
        
        # step 2: merge
        # head -> second -> head.next -> second.next
        
        dummy = None # store leftovers of second list while merging
        curr = head

        while curr.next and second.next: # 1-2-n, 4-3-n
            tmp = curr.next # -2-n
            curr.next = second # 1->4-3-n
            dummy = second.next # -3-n
            second.next = tmp # 1-4->2-n

            second = dummy # -3-n
            curr = tmp # -2-n
    


        

        






