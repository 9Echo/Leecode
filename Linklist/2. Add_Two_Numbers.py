
"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
"""
# 该代码参考Leecode题解，将python的简洁应用到极致
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            # 直接用s来存储和，不需要额外的sum来存储（s最大是9+9+1=19，整除10后仍然是取0或1）
            # 代码相当简洁
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next
            s //= 10
            # 代码相当简洁
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
