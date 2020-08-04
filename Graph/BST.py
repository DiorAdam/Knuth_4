class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self,inputValues):
        self.root = TreeNode(inputValues[0])
        nodeQueue = [self.root]
        front = 0
        index = 1
        while index < len(inputValues):
            node = nodeQueue[front]
            front = front + 1

            item = inputValues[index]
            index = index + 1
            if not item is None:
                leftNumber = item
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)

            if index >= len(inputValues):
                break

            item = inputValues[index]
            index = index + 1
            if not item is None :
                rightNumber = item
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
    
    def prettyPrintTree(self, node=-1, prefix="", isLeft=True):
        if node == -1: node = self.root
        if not node:
            print("Empty Tree")
            return

        if node.right:
            self.prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

        print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

        if node.left:
            self.prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)
    
        
    def height(self, head = -1):
        if head == -1: head = self.root
        if head is None: return -1
        return 1 + max(self.height(head.left),self.height(head.right))
    
    def order(self, head = -1):  #return the amount of vertices in self.root
        def helper(head=self.root):
            if head is None: return 0
            return 1 + helper(head.left) + helper(head.right)
        return helper()

    def searchInsert(self, val):
        '''recursive version
        def helper(head = self.root):
            if not head : return TreeNode(val)
            if head.val == val:
                print(str(val)+ " is already in the BST root")
                return head
            elif head.val > val:
                head.left = helper(head.left)
            else:
                head.right = helper(head.right)
            return head
        self.root = helper()
        '''
        #iterative version
        head = self.root
        while True:
            if head.val == val: 
                print(str(val)+ " is already in the BST root")
                return 
            elif head.val > val:
                if head.left: head = head.left
                else: break
            else: 
                if head.right: head = head.right
                else : break
        if head.val > val: head.left = TreeNode(val)
        else: head.right = TreeNode(val) 



    def delete(self, val):
        Q = self.root
        while Q and Q.val != val:
            if Q.val > val:
                Q = Q.left
            else:
                Q = Q.right
        if not Q:
            print(str(val) + " is not in self.root")
            return 
        T = Q
        R = T.right
        if not R:
            T = T.left
        elif not R.left:
            R.left = T.left
            T=R
        else:
            S = R.left
            while S.left:
                R = S
                S = S.left
            S.left = T.left
            R.left = S.right
            S.right = T.right
            T = S
        Q.val = T.val
        Q.left = T.left
        Q.right = T.right
    



        
        
        


zodiac = ["CAPRICORN", "AQUARIUS", "PISCES", "PISCES", "ARIES", "TAURUS", "GEMINI", "CANCER", "LEO", "VIRGO", "LIBRA", "SCORPIO"]
permutation = [1,-3,4,5,-5,-1,0,2,-6,-2,-4]
zigzag = []
for x in permutation:
    zigzag.append(zodiac[x])

inorder = sorted(zodiac)

def represent(l):
    u = BST([l[0]])
    for val in l:
        u.searchInsert(val)
    u.delete("PISCES")
    u.prettyPrintTree()
    #print(u.order())
    #print(u.height())

represent(zodiac)


    


    


