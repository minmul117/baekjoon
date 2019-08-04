#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.72%)
# Total Accepted:    794K
# Total Submissions: 2.6M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        leading_one = 0; left = l1; right = l2
        return_head = ListNode(0)
        curr = return_head
        while left is not None or right is not None:
            sums = 0
            if left is not None:
                sums += left.val
            if right is not None:
                sums += right.val

            sums += leading_one
            leading_one = 1 if sums >= 10 else 0

            if sums >= 10:
                sums -= 10
            
            curr.next = ListNode(sums)
            curr = curr.next
            
            if left is not None and left.next is not None:
                left = left.next
            else:
                left = None

            if right is not None and right.next is not None:
                right = right.next
            else:
                right = None
        
        if leading_one == 1:
            curr.next = ListNode(1)

        return return_head.next
            