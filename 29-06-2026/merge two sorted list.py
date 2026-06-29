# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

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

def mergeTwoList(first:ListNode,second:ListNode)->ListNode:
    dummy = ListNode()
    current = dummy

    while first and second:
        if first.val > second.val:
            current.next = second
            second = second.next
        else:
            current.next = first
            first = first.next
        current=  current.next

    if first:
        current.next = first

    if second:
        current.next = second

    return dummy.next

l1 = addElements([1,2,3,4])
l2 = addElements([1,3,5])

add = mergeTwoList(l1,l2)
printList(add)

