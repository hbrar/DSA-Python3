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

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

# Non recursive solution - 1

stck = []
def inOrder_nr(root):
    currRoot = root
    done = False
    
    while not done:
        if currRoot != None:
            stck.append(currRoot)
            currRoot =  currRoot.left
        else:
            if len(stck) > 0:
                #backtrack
                currRoot = stck.pop() 
                print(currRoot.val)
                currRoot = currRoot.right
            else:
                done = True

# Non recursive solution - 2

def inOrder_nr2(root):
    """Each node will be visited twice except the leaf nodes. Now for an algo where every node is visited twice, comlexity will be O(2n)  => O(n)..for this algo it's n< this< 2n
    Hence complexity is O(n)"""
    
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
            # => it's a leaf node OR if you have already checked it's children implies you have placed them in order LEFT <- PARENT <- RIGHT in stack 
            # then being at this point means you have processed left child and are currently at parent...so push it's value to output[] for traversal to be inorder
            output.append(root.val)
        else:
            if root.right != None:
                stck.append((root.right,False))
                
            stck.append((root, True))   
            
            if root.left !=  None:
                stck.append((root.left,False))
        # print(stck)
        # print(output)

    return output       
        


print("="*10,"Tree 1","="*10)
print("-"*10,"Recursive","-"*10)
inOrder(root)
print("-"*10,"Non-Recursive","-"*10)
inOrder_nr(root)
print("-"*10,"Non-Recursive","-"*10)
print(inOrder_nr2(root))

print("="*10,"Tree 2","="*10)
print("-"*10,"Recursive","-"*10)
inOrder(root1)
print("-"*10,"Non-Recursive","-"*10)
inOrder_nr(root1)
print("-"*10,"Non-Recursive","-"*10)
print(inOrder_nr2(root1))