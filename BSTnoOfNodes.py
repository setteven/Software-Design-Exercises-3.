class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#A function to count no. of nodes.
def counter(root,count):
    if root:
        #First recur the left child
        if root.left:
            count=counter(root.left,count)
        count+=1
        #Recur the right child at last
        if root.right:
            count=counter(root.right,count)
        return count

def main():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)
    root.left.right.right = Node(7)
    count=0
    count=counter(root,count)
    print('The no. of nodes in the tree are = ',count)

#Driver code
if __name__ == "__main__":
    main()