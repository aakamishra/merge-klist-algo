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
        Iterative solution of solving the merge klists problem.

        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # create object for storing values from all lists
        final_list = []

        # iterate through the list of linkedlists and dump values into list
        for list in lists:
            curr = list
            while curr:
                final_list.append(curr.val)
                curr = curr.next

        # get total count of all values in list
        n = len(final_list)

        # create new head for storing final returned linked list
        return_ptr = new_head = ListNode(val=-1)

        # iterative O(n^2) solution for sorting final list
        for i in range(n):
            for j in range(i + 1, n):
                if final_list[i] > final_list[j]:
                    temp = final_list[i]
                    final_list[i] = final_list[j]
                    final_list[j] = temp
            # per sorted value, add new node
            new_head.next = ListNode(val=final_list[i])
            new_head = new_head.next

        # return final list
        return return_ptr.next

    def recursive_merge_k_lists(self, lists):
        """
        Recursive solution to the merge klists problem.

        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def combine_helper(a, b):
            """
            Helper function to merge two linked lists recursively

            :type a: ListNode
            :type b: ListNode
            :rtype return_ptr: ListNode
            """
            if not a and not b:
                return None
            elif a and not b:
                return a
            elif b and not a:
                return b
            elif a and b:
                # conditions for mantainin order invariant
                if a.val <= b.val:
                    a.next = combine_helper(a.next, b)
                    return a
                if a.val > b.val:
                    b.next = combine_helper(a, b.next)
                    return b

        # create new head of the final list to return
        return_ptr = combined_list = ListNode(val=-1)

        # iterate over each list and sequentially merge them
        for ls in lists:
            combine_helper(combined_list, ls)

        # return head of the final product
        return return_ptr.next


class MergeKListsTest:
    """
    Class for testing solution code from the solution class
    with given test parameters for a LinkedList

    :type expected_input: list
    :type expected_output: list
    :type solution_method: lambda
    """

    def __init__(
            self,
            expected_input,
            expected_output,
            solution_method) -> None:
        self.expected_input = expected_input
        self.expected_output = expected_output
        self.method = solution_method
        self.run_test_case()

    def list_parser(self, current: ListNode) -> list:
        """
        Function to translate from linked list to pythonic list

        :type current: ListNode
        """
        final_list = []

        # iterate over linked list and store final values
        while current:
            final_list.append(current.val)
            current = current.next

        return final_list

    def input_generator(self):
        """
        Takes multi-dimensional input and output linkedlists.
        """
        curr = return_ptr = ListNode(val=-1)
        list_of_lists = []

        # iterate over expected input
        for input_list in self.expected_input:
            # establish the head of the list
            curr = return_ptr = ListNode(val=-1)

            # add values into the new linked list
            for val in input_list:
                curr.next = ListNode(val=val)
                curr = curr.next
            list_of_lists.append(return_ptr.next)

        return list_of_lists

    def check_output(self, output):
        """
        Converts between linked list and list to check equivalence.

        :type output: ListNode
        """
        assert self.list_parser(output) == self.expected_output

    def run_test_case(self):
        """
        Runs logic of input and output conversion as well as
        running the actual algo. Checks answer output
        and benchmarks the time.
        """

        print("Running Test Case")
        # generate input
        input = self.input_generator()

        print("Test Input: ", self.expected_input)
        start = time.time()
        test_output = self.method(input)
        end = time.time()

        # print logging for answers
        print("Recieved Output: ", self.list_parser(test_output))
        print("Expected Output: ", self.expected_output)

        # ensure the expectation is met
        try:
            self.check_output(test_output)
            print("Test Case Passed!")
        except AssertionError as e:
            print("Test Case Failed: ", e)

        print("Test Time Elapsed: ", end - start, " seconds")
        print("----------------------------")


if __name__ == "__main__":
    # unit test cases for the iterative solution
    print("TEST CASES FOR ITERATIVE SOLUTION")
    print("---------------------------------")
    MergeKListsTest(expected_input=[[1, 4, 5], [1, 3, 4], [2, 6]],
                    expected_output=[1, 1, 2, 3, 4, 4, 5, 6],
                    solution_method=Solution().iterative_merge_k_lists)

    MergeKListsTest(expected_input=[[1, 3, 4], [1, 3, 4]],
                    expected_output=[1, 1, 3, 3, 4, 4],
                    solution_method=Solution().iterative_merge_k_lists)

    MergeKListsTest(expected_input=[[1, 4, 15, 19], [1, 3, 4, 5, 6]],
                    expected_output=[1, 1, 3, 4, 4, 5, 6, 15, 19],
                    solution_method=Solution().iterative_merge_k_lists)

    # unit test cases for the recursive solution
    print("TEST CASES FOR RECURSIVE SOLUTION")
    print("---------------------------------")
    MergeKListsTest(expected_input=[[1, 4, 5], [1, 3, 4], [2, 6]],
                    expected_output=[1, 1, 2, 3, 4, 4, 5, 6],
                    solution_method=Solution().recursive_merge_k_lists)

    MergeKListsTest(expected_input=[[1, 3, 4], [1, 3, 4]],
                    expected_output=[1, 1, 3, 3, 4, 4],
                    solution_method=Solution().recursive_merge_k_lists)

    MergeKListsTest(expected_input=[[1, 4, 15, 19], [1, 3, 4, 5, 6]],
                    expected_output=[1, 1, 3, 4, 4, 5, 6, 15, 19],
                    solution_method=Solution().recursive_merge_k_lists)
