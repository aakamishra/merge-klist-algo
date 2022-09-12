"""
You are given an array of k linked-lists lists, each linked-list
is sorted in ascending order. Merge all the linked-lists into
one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

"""

import time


class ListNode(object):
    """
    ListNode class for implementing linked lists
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def iterative_merge_k_lists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        final_list = []
        for list in lists:
            curr = list
            while curr:
                final_list.append(curr.val)
                curr = curr.next
        n = len(final_list)
        return_ptr = new_head = ListNode(val=-1)
        for i in range(n):
            for j in range(i + 1, n):
                if final_list[i] > final_list[j]:
                    temp = final_list[i]
                    final_list[i] = final_list[j]
                    final_list[j] = temp
            new_head.next = ListNode(val=final_list[i])
            new_head = new_head.next
        return return_ptr.next

    def recursive_merge_k_lists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def combine_helper(a, b):
            if not a and not b:
                return None
            elif a and not b:
                return a
            elif b and not a:
                return b
            elif a and b:
                if a.val <= b.val:
                    a.next = combine_helper(a.next, b)
                    return a
                if a.val > b.val:
                    b.next = combine_helper(a, b.next)
                    return b

        return_ptr = combined_list = ListNode(val=-1)
        for ls in lists:
            combine_helper(combined_list, ls)

        return return_ptr.next


class MergeKListsTest:
    """
    Class for testing solution code from the solution class
    with given test parameters for a LinkedList
    """

    def __init__(
            self,
            expected_input,
            expected_output,
            solution_method) -> None:
        self.expected_input = expected_input
        self.expected_output = expected_output
        self.method = solution_method

    def list_parser(self, current: ListNode) -> list:
        final_list = []
        while current:
            final_list.append(current.val)
            current = current.next

        return final_list

    def input_generator(self):
        curr = return_ptr = ListNode(val=-1)
        list_of_lists = []
        for input_list in self.expected_input:
            curr = return_ptr = ListNode(val=-1)
            for val in input_list:
                curr.next = ListNode(val=val)
                curr = curr.next
            list_of_lists.append(return_ptr.next)

        return list_of_lists

    def check_output(self, output):
        assert self.list_parser(output) == self.expected_output

    def run_test_case(self):
        print("Running Test Case")
        input = self.input_generator()
        print("Test Input: ", self.expected_input)
        start = time.time()
        test_output = self.method(input)
        end = time.time()
        print("Recieved Output: ", self.list_parser(test_output))
        print("Expected Output: ", self.expected_output)
        try:
            self.check_output(test_output)
            print("Test Case Passed!")
        except AssertionError as e:
            print("Test Case Failed: ", e)

        print("Test Time Elapsed: ", end - start, " seconds")
        print("----------------------------")
