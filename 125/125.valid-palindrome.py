#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True
        removed_str = (''.join(e for e in s if e.isalnum())).lower()
        reversed_removed_str = removed_str[::-1]
        return removed_str == reversed_removed_str