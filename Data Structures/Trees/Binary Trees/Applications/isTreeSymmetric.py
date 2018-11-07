import sys 
sys.path.append('..')
import BTreeNode

"""
create tree

      1
   2     2
3    4  4    3
"""
root = BTreeNode.BTreeNode(1)
root.left = BTreeNode.BTreeNode(2)
root.left.left =  BTreeNode.BTreeNode(3)
root.left.right = BTreeNode.BTreeNode(4)
root.right =  BTreeNode.BTreeNode(2)
root.right.right = BTreeNode.BTreeNode(3)
root.right.left = BTreeNode.BTreeNode(4)


"""
create tree

        1
   2        2
      3       3
"""
root1 = BTreeNode.BTreeNode(1)
root1.left = BTreeNode.BTreeNode(2)
root1.right = BTreeNode.BTreeNode(2)
root1.left.right = BTreeNode.BTreeNode(3)
root1.right.right = BTreeNode.BTreeNode(3)

# Recursive solution


def isTreeSymmetric(root):
    # output = "" immutable variables (strings here) can't be bind in inner scope
    output = []
    inOrder(root,output)
    return isPalindrome(output)
    
def inOrder(root,output):
    if root != None:
        inOrder(root.left,output)
        output.append(str(root.val))
        inOrder(root.right,output)

def isPalindrome(inp):
    return "".join(inp) == "".join(reversed(inp))

"""
Fails for

        1
   2        3
3         2      
"""   
root3 = BTreeNode.BTreeNode(1)
root3.left = BTreeNode.BTreeNode(2)
root3.right = BTreeNode.BTreeNode(3)
root3.left.left = BTreeNode.BTreeNode(3)
root3.right.left = BTreeNode.BTreeNode(2)


print(isTreeSymmetric(root))
print(isTreeSymmetric(root1))
print(isTreeSymmetric(root3))

##########Better solution and does not fail

def isTreeSymmetric2(root):
    return isMirror(root, root)

def isMirror(root1, root2):
    if root1 == None and root2 == None:
        return True
    
    if root1 != None and root2 != None:
        if root1.val == root2.val:
            return (isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left))
        
    return False
     
print("*"*30)
print(isTreeSymmetric2(root))
print(isTreeSymmetric2(root1))
print(isTreeSymmetric2(root3))