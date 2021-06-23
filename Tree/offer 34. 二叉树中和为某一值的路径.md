## [Offer 34. 二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)

题目描述：输入一棵二叉树，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

### 思路一：直接dfs递归

遍历所有完整的根节点至叶子节点的路径，如果和为给定值，那么保留这条路径。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []

        res = []

        def dfs(root, path):
            if not root.left and not root.right and sum(path) == target:
                res.append(path)
            
            if root.left:
                dfs(root.left, path + [root.left.val])
            if root.right:
                dfs(root.right, path + [root.right.val])
        
        dfs(root, [root.val])
        return res
```

注意这里的res不需要考虑全局变量、局部变量，是因为python内部数组（list）本身是可变类型。所以不需要self。