# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


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

    print("===LIST===")
    while start:
        print(start.val,end="")
        start = start.next
    print("\n========")


def removeDuplicated(head:ListNode)->ListNode:
    dummy = ListNode(-1,head) # cuz range is 0-300
    current = dummy

    while current:
        while current.next and current.val == current.next.val:
            current.next = current.next.next
        current = current.next

    return dummy.next


li = addElements([1,1,2,2,2,3])
printList(li)

l = removeDuplicated(li)

printList(l)
