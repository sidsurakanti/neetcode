"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # wo random
        hmap = dict()
        def copy(curr):
            if not curr:
                return None

            new = Node(curr.val, copy(curr.next))
            hmap[curr] = new # fill for random pass
            return new
        
        new_head = copy(head)
        
        # debug
        # for k, v in hmap.items():
        #     print(k.val, k.random)

        curr = head
        while curr:
            if curr.random:
                hmap[curr].random = hmap[curr.random]
            curr = curr.next

        return new_head
            
            

        


