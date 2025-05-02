# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head

        values = []

        # Collect values from odd-indexed nodes (1-based: positions 1,3,5,...)
        temp = head
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break

        # Collect values from even-indexed nodes (1-based: positions 2,4,6,...)
        temp = head.next
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break

        # Assign values back to the list
        temp = head
        index = 0
        while temp is not None:
            temp.val = values[index]
            index += 1
            temp = temp.next

        return head

        
        """
class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even  # To reconnect later

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head
