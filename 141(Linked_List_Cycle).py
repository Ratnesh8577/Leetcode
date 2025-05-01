# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Brute Solution 
"""
class Solution(object):
    def hasCycle(self, head):
        temp= head 
        my_set=set()
        while temp is not None:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp=temp.next
        return False
"""

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False



        