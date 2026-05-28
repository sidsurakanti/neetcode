# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        # make i the smaller of the two to start
        if list1.val <= list2.val:
            i = list1
            j = list2
            k = list1
        else:
            i = list2
            j = list1
            k = list2

        while i.next != None:
            if not j:
                return k

            # SCENARIO list 2 has items
            # compare l2_i and l1_{i + 1}
            if i.next.val > j.val:
                # insert j between i and i.next
                jn1 = j.next
                j.next = i.next
                i.next = j

                # move ahead on l2 
                j = jn1
            
            i = i.next
        
        # append rest of l2 to l1
        i.next = j
        
        return k

            
        
            
            
                

         

        