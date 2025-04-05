# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None 
            return mid

        def merge(l, r):
            dummy = ListNode()
            tail = dummy
            while l and r:
                if l.val <= r.val:
                    tail.next = l
                    l = l.next
                else:
                    tail.next = r
                    r = r.next
                tail = tail.next

            tail.next = l if l else r
            return dummy.next

        mid = split(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)

            