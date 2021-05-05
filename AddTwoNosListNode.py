# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:
            return l2
        if l2==None:
            return l1
        sum1=l1.val+l2.val
        if sum1<10:
            data=ListNode(sum1)
            data.next=self.addTwoNumbers(l1.next,l2.next)
            return data
        else:
            carry=l1.val+l2.val-10
            data=ListNode(carry)
            data.next=self.addTwoNumbers(ListNode(1),self.addTwoNumbers(l1.next,l2.next))
            return data
        
        
