'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def deleteNode(self, head, x):
        if(x == 1):
            temp = head
            head = head.next
            temp.next = None
        else:
            prev = head
            for _ in range(x-2):
                prev = prev.next
        
            temp = prev.next
            prev.next = temp.next
            temp.next = None
        
        return head