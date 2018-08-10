'''
https://leetcode.com/problems/palindrome-linked-list/description/

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPallindrome(self, head):
        fast, slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            nxt = slow.next
            slow.next=node
            node = slow
            slow=nxt

        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
