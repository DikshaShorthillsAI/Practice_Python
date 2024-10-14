import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0) 
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next

def list_to_linkedlist(lst):
    """Converts a list to a linked list."""
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    """Converts a linked list back to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_two_sorted_lists(self):
        # Test case 1: Merging [1,2,4] and [1,3,4]
        list1 = list_to_linkedlist([1, 2, 4])
        list2 = list_to_linkedlist([1, 3, 4])
        merged_list = self.solution.mergeTwoLists(list1, list2)
        result = linkedlist_to_list(merged_list)
        self.assertEqual(result, [1, 1, 2, 3, 4, 4])

    def test_empty_lists(self):
        # Test case 2: Merging two empty lists
        list1 = list_to_linkedlist([])
        list2 = list_to_linkedlist([])
        merged_list = self.solution.mergeTwoLists(list1, list2)
        result = linkedlist_to_list(merged_list)
        self.assertEqual(result, [])

    def test_one_empty_list(self):
        # Test case 3: Merging empty list with [0]
        list1 = list_to_linkedlist([])
        list2 = list_to_linkedlist([0])
        merged_list = self.solution.mergeTwoLists(list1, list2)
        result = linkedlist_to_list(merged_list)
        self.assertEqual(result, [0])

    def test_identical_lists(self):
        # Test case 4: Merging two identical lists [2, 3, 5]
        list1 = list_to_linkedlist([2, 3, 5])
        list2 = list_to_linkedlist([2, 3, 5])
        merged_list = self.solution.mergeTwoLists(list1, list2)
        result = linkedlist_to_list(merged_list)
        self.assertEqual(result, [2, 2, 3, 3, 5, 5])

    def test_single_element_lists(self):
        # Test case 5: Merging [1] and [2]
        list1 = list_to_linkedlist([1])
        list2 = list_to_linkedlist([2])
        merged_list = self.solution.mergeTwoLists(list1, list2)
        result = linkedlist_to_list(merged_list)
        self.assertEqual(result, [1, 2])

if __name__ == "__main__":
    unittest.main()
