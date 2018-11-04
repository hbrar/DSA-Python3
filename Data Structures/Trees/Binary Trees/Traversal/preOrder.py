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
"""
root1 = BTreeNode.BTreeNode('r')
root1.left = BTreeNode.BTreeNode('r1')
root1.right = BTreeNode.BTreeNode('r2')
root1.left.right = BTreeNode.BTreeNode('r3')
root1.right.left = BTreeNode.BTreeNode('r4')

# recursive solution
def preOrder(root):
    if root != None:
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)
        
def preOrder_nr(root):
    stck = []
    output = []
    
    if root == None:
        return output
    
    stck.append(root)
    
    while stck:
        root = stck.pop()
        output.append(root.val) #parent
        
        if root.right != None:
            stck.append(root.right)
        if root.left != None:
            stck.append(root.left)
    return output

print("="*10,"Tree 1","="*10)
print("-"*10,"Recursive","-"*10)
preOrder(root)
print("-"*10,"Non-Recursive","-"*10)
print(preOrder_nr(root))


print("="*10,"Tree 2","="*10)
print("-"*10,"Recursive","-"*10)
preOrder(root1)
print("-"*10,"Non-Recursive","-"*10)
print(preOrder_nr(root1))
