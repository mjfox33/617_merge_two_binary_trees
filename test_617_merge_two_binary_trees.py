import code_617_merge_two_binary_trees as c

def test_example_1():
    s=c.Solution()
    root1 = c.TreeNode(1, c.TreeNode(3,4,None), c.TreeNode(2,None,None))
    root2 = c.TreeNode(2, c.TreeNode(1,None,4), c.TreeNode(3,None,7))
    ans = c.TreeNode(3, c.TreeNode(4,5,4), c.TreeNode(5,None,7))
    merged = s.mergeTrees(root1, root2)
    assert merged == ans