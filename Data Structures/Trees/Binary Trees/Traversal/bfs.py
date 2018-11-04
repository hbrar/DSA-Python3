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

def bfs(root):
    if root is None:
        return []
        
    parentStck = []
    childStack = []
    output = []
    childStack.append(root)
    done = False
    
    while not done:
        
        lvlElements = []
        
        #parentStck and childStck won't be empty at same time unless finished
        while childStack:
            el = childStack.pop()
            lvlElements.append(el.val)
            parentStck.append(el)
            
        while parentStck:
            el = parentStck.pop()
            if el.right != None:
                childStack.append(el.right)
            if el.left != None:
                childStack.append(el.left)
                
        output.append(lvlElements)
        
        if not parentStck and not childStack:
            done = True
        
    return output        

print("="*10,"Tree 1","="*10)
print(bfs(root))
print("="*10,"Tree 2","="*10)
print(bfs(root1))

class Queue:
    def __init__(self):
        self.__q = []
        self.__head = 0
        self.__tail = 0
        
    def __len__(self):
        return self.__tail - self.__head
        
    def enqueue(self, x):
        self.__q.append(x)
        self.__tail += 1
        
    def dequeue(self):
        out = self.__q[self.__head]
        self.__head += 1
        return out
        
# faster than bfs()
def bfs2(root):
    if root is None:
        return []
        
    q = Queue()
    output = []
    q.enqueue(root)
    done = False
    while len(q) > 0:
        parent = q.dequeue()
        output.append(parent.val)
        
        if parent.left != None:
            q.enqueue(parent.left)
        if parent.right != None:
            q.enqueue(parent.right)

    return output  

print("="*10,"Tree 1","="*10)
print(bfs2(root))
print("="*10,"Tree 2","="*10)
print(bfs2(root1))

# Same as above just, customized output
def bfs3(root):
    if root is None:
        return []
            
    q = Queue()
    output = []
    q.enqueue(root)
    q.enqueue("EOL")
    done = False
    lvlElements = []

    while len(q) > 0:
        parent = q.dequeue()
        if parent != "EOL":
            lvlElements.append(parent.val)
            if parent.left != None:
                q.enqueue(parent.left)
            if parent.right != None:
                q.enqueue(parent.right)
        elif parent == "EOL" and len(q) > 0:
            output.append(lvlElements)
            lvlElements = []
            q.enqueue("EOL")
        else:
            output.append(lvlElements)
            
    return output
    
print("="*10,"Tree 1","="*10)
print(bfs3(root))
print("="*10,"Tree 2","="*10)
print(bfs3(root1))