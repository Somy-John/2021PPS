# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        while True:
            if head==None: break
            else:
                nodes.append(head.val)
                head = head.next
        if len(nodes) == 0: return
        
        return nodes == list(reversed(nodes))