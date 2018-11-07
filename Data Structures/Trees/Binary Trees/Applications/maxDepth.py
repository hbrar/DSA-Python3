import BTreeNode

"""
create tree

      4
   5     9
6    7      11
"""
root = BTreeNode.BTreeNode(4)
root.left = BTreeNode.BTreeNode(5)
root.left.left =  BTreeNode.BTreeNode(6)
root.left.right = BTreeNode.BTreeNode(7)
root.right =  BTreeNode.BTreeNode(9)
root.right.right = BTreeNode.BTreeNode(11)

"""
create tree

        'r'
   'r1'     'r2'
      'r3' 'r4'   
    'r5'
"""
root1 = BTreeNode.BTreeNode('r')
root1.left = BTreeNode.BTreeNode('r1')
root1.right = BTreeNode.BTreeNode('r2')
root1.left.right = BTreeNode.BTreeNode('r3')
root1.left.right.left = BTreeNode.BTreeNode('r5')
root1.right.left = BTreeNode.BTreeNode('r4')

# Recursive
depth = 0

def maxDepth(root, currheight = 1):
    if root != None:
        if currheight >= globals()['depth']:
            globals()['depth'] = currheight
        maxDepth(root.left, currheight + 1)
        maxDepth(root.right, currheight + 1)
    
maxDepth(root)
print(depth)
depth = 0
maxDepth(root1)
print(depth)
    