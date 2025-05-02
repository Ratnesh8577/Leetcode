# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        temp = head
        while temp is not None:
            length+=1
            temp = temp.next
        if length == n:
            new_head=head.next
            del head
            return new_head
        position_to_stop=length-n
        temp=head
        count=1
        while count<position_to_stop:
            temp=temp.next
            count+=1
        temp.next=temp.next.next
        return head
       """

class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow= head 
        fast=head
        for _ in range(n):
            fast = fast.next
        if fast==None:
            return head.next
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head

