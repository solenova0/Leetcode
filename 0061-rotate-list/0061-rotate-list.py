# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        slow = fast = head
        length = 1

        while k and fast.next:
            fast = fast.next
            length += 1
            k -= 1

        if k != 0:
            k = (k + length - 1) % length # original k % length
            return self.rotateRight(head, k)
        else:
            while fast.next:
                fast = fast.next
                slow = slow.next
            return self.rotate(head, fast, slow)

    def rotate(self, head, fast, slow):
        fast.next = head
        head = slow.next
        slow.next = None
        return head