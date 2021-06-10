## 二叉树遍历

二叉树的遍历方法一共两种，深度优先（dfs）和广度优先（bfs），其中深度优先遍历根据父结点的遍历顺序分为先序、中序、后序遍历三种，广度优先遍历即层次遍历。

dfs对应的三种顺序的遍历大致两种方法：递归和迭代（还有一种方法：Morris遍历，可以实现线性时间与常数空间的遍历，还没开始看==）

### 深度优先遍历

**方法1：递归**

深度优先搜索：左→存储→右

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        def dfs(root):
            if not root:
                return 
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res
```

**方法2：迭代**

> 树的迭代思路为，引入栈结构，root节点入栈，一直遍历其左节点（入栈）直到左节点为空，再出栈依次遍历其右节点。

前中序遍历的区别在于遍历的过程中**何时存储节点值**

后序遍历稍微麻烦，不同于前序、中序遍历，后序遍历过程中需要从当前节点回退到该节点的父结点这一过程，但树结构本身并不能直接访问父结点，所以利用栈来存储父结点，栈顶即root节点。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        ans = []
        while root or ans:
            if root:
                ans.append(root)
                root = root.left
            else:
                root = ans.pop()
                res.append(root.val)
                root = root.right
        return res
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        ans = []
        while root or ans:
            if root:
                res.append(root.val)
                ans.append(root)
                root = root.left
            else:
                root = ans.pop()
                root = root.right
                
        return res
    
    def postdorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return list()
        
        res = list()
        ans = list()
        #prev用来记录当前子节点是否被记录了
        prev = None
        while root or ans:
            # 遍历到最左的左子节点
            while root:
                ans.append(root)
                root = root.left
            root = ans.pop()
            # 如果没有该节点没有右节点而且该节点没有被遍历过，就保存该节点
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                # 否则该节点入栈，遍历其右节点（右子树）
                ans.append(root)
                root = root.right
                
        return res
```

#### 错误

- `res`用于存储结果，应该是存储`root.val`

### 广度优先遍历（层次遍历）

> BFS同样需要借助栈来临时存储节点，思路很简单，遍历当前层数，记录当前层数节点的所有子节点，需要记录当前层数有多少个子节点。

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        cur = [root]
        while cur:
            length = len(cur)
            tmp = []
            for i in range(length):
                node = cur.pop(0)
                tmp.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
           res.append(tmp)
        return res
```

还有一个很有意思的dfs递归写法

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        # index 表示当前层数
        def dfs(index, node):
            # res=[[1], [2, 3]]时，index为3，需要插入一个空list
            if len(res) < index:
                res.append([])
            res[index-1].append(node.val)
            if node.left:
                dfs(index+1, node.left)
            if node.right:
                dfs(index+1, node.right)
        dfs(1, root)
        return res
```

