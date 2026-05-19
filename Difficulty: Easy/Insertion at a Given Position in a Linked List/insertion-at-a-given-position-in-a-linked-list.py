'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def insertPos(self, head, pos, value):
        new_node = Node(value)
        
        if(pos == 1):
            new_node.next = head
            head = new_node
        else:
            temp = head
            for _ in range(pos - 2):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        
        return head
      
      