# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.recurse(head)

    def recurse(self, node, prev=None):
        if not node:
            return prev
        else:
            h = node.next
            node.next = prev
            return self.recurse(h, node)
