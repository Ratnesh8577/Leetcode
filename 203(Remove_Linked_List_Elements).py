# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> optional[listNode]:
        # Create a dummy node to simplify deletion at head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        # Traverse the list and remove nodes with value equal to `val`
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next  # Remove the node
            else:
                current = current.next  # Move to the next node

        return dummy.next
