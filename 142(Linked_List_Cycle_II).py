# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Brute Solution 
"""
class Solution(object):
    def detectCycle(self, head):
        temp = head
        my_set= set()
        while temp is not None:
            if temp in my_set:
                return temp
            my_set.add(temp)
            temp = temp.next
        return None
     """
class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  
        return None
