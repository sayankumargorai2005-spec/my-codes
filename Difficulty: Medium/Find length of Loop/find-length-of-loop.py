class Solution:
    def lengthOfLoop(self, head):
        
        if head is None or head.next is None:
            return 0

        slow = head
        fast = head

    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                
                
                count = 1
                temp = slow.next

                while temp != slow:
                    count += 1
                    temp = temp.next

                return count
            
        return 0
        