#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (46.23%)
# Total Accepted:    531.8K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root_node = ListNode(0)
        t_r = root_node
        t_l1 = l1
        t_l2 = l2
        while(t_l1 is not None and t_l2 is not None):
            if t_l1.val > t_l2.val:
                cur_val = t_l2.val
                t_l2 = t_l2.next
            else:
                cur_val = t_l1.val
                t_l1 = t_l1.next
            t_r.next = ListNode(cur_val)
            t_r = t_r.next
        if t_l1 is None:
            t_r.next = t_l2
        else:
            t_r.next = t_l1
        return root_node.next
