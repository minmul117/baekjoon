#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (45.12%)
# Total Accepted:    129.9K
# Total Submissions: 286.8K
# Testcase Example:  '2'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
# 
# Given a non-negative integer n representing the total number of bits in the
# code, print the sequence of gray code. A gray code sequence must begin with
# 0.
# 
# Example 1:
# 
# 
# Input: 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# 
# For a given n, a gray code sequence may not be uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence.
# 
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
# 
# 
# Example 2:
# 
# 
# Input: 0
# Output: [0]
# Explanation: We define the gray code sequence to begin with 0.
# A gray code sequence of n has size = 2^n, which for n = 0 the size is 2^0 =
# 1.
# Therefore, for n = 0 the gray code sequence is [0].
# 
# 
#
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # n = 0 : [0]
        # n = 1 : [0, 1]
        # n = 2 : [0, 1, 3, 2] 
        # n = 3 : [0, 1, 3, 2, 6, 7, 5, 4]
        # 이전 리스트를 리버스, 그 다음 2^(n-1)을 기존 리스트 원소워 더한 값들이다.
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]
        return results

