import sys 
sys.path.append('..')
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

# Recursive solution

def postOrder(root):
    if root != None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val)

# Non recursive solution 

def postOrder_nr2(root):
    stck = []
    output = []
    
    if root == None:
        return output
    # passing False if not checked children yet
    stck.append((root,False))
    
    while stck:
        rootTuple = stck.pop()
        root = rootTuple[0]
        checkedChildren = rootTuple[1]
        
        if (checkedChildren == True or (root.left == None and root.right == None)):
            output.append(root.val)
        else:
            stck.append((root, True))
            
            if root.right != None:
                stck.append((root.right,False))
            
            if root.left !=  None:
                stck.append((root.left,False))

    return output       
        


print("="*10,"Tree 1","="*10)
print("-"*10,"Recursive","-"*10)
postOrder(root)
print("-"*10,"Non-Recursive","-"*10)
print(postOrder_nr2(root))

print("="*10,"Tree 2","="*10)
print("-"*10,"Recursive","-"*10)
postOrder(root1)
print("-"*10,"Non-Recursive","-"*10)
print(postOrder_nr2(root1))