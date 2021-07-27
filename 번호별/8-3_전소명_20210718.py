# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        nodes = []
        while True:
            if head==None: break
            else:
                nodes.append(head.val)
                head = head.next
        if len(nodes) == 0: return
        rstTmp = ListNode()
        rst = rstTmp
        nodes.reverse()
        for n in nodes[:-1]:
            rstTmp.val = n
            tmp = ListNode()
            rstTmp.next = tmp
            rstTmp = tmp
        rstTmp.val = nodes[-1]
        return rst