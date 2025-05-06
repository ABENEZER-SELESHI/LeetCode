# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heqp = []

        for link in lists:
            while link:
                heappush(heqp, link.val)
                link = link.next
        
        dummy = ListNode(-1)
        # dummy.next = None
        # return dummy
        curr = dummy

        while heqp:
            dummy.next = ListNode(heappop(heqp))
            dummy = dummy.next
        
        return curr.next