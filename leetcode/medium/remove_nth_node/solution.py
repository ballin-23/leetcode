# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        copy = head
        arr = []
        while head:
            arr.append(head)
            head = head.next
        if len(arr) > n:
            index = (len(arr) -1) -n
            arr[index].next = arr[index+1].next
        else:
            if len(arr) == 1 and n == 1:
                return None
            elif len(arr) == n:
                index = len(arr)- n
                if index == 0:
                    copy = arr[index+1]
                else:
                    arr[index-1].next = arr[index].next
        return copy