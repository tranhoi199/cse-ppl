class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def count(root):
    if root is None:
        return 0
    else:
        return 1 + count(root.left) + count(root.right)

def sum(root):
    if root is None:
        return 0
    else:
        return root.val + sum(root.left) + sum(root.right)

        
ex = Node(3,Node(4,Node(5)),Node(10))  

print(count(ex))  
print(sum(ex))  