# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# Constraints:
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

# what are the edge cases we have two first is first node to remove and second is lastnode to remove
# for between we can directly remove the element

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addElements(nums:list)->ListNode:
    dummy = ListNode()
    current = dummy

    for num in nums:
        current.next = ListNode(num)
        current = current.next

    return dummy.next

def printList(head:ListNode)->None:
    start = head
    print("==List==")
    while start:
        print(start.val,end="")
        start = start.next
    print("\n========")

def deleteListElements(head:ListNode,val:int)->ListNode:
    dummy = ListNode(0,head)
    current = dummy

    while current:
        while current.next and current.next.val == val:
            current.next = current.next.next
        current = current.next

    return dummy.next


li = addElements([1,2,6,3,4,5,6])
printList(li)

deleteListElements(li,6)
printList(li)
