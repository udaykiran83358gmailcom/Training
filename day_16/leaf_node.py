class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def create(self,data):
        if self.root is None:
            self.root=node(data)
        else:
            self.insertion(self.root,data)
    def insertion(self,root,data):
        if root.data>data:
            if root.left==None:
                root.left=node(data)
            else:
                self.insertion(root.left,data)
        else:
            if root.right==None:
                root.right=node(data)
            else:
                self.insertion(root.right,data)
    def inorder(self):
        stack=[]
        curr=self.root
       
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            
            curr=stack.pop()
            print(curr.data)
            curr=curr.right
    def preorder(self):
        node=self.root
        stack=[node]
        while stack:
            curr=stack.pop()
            print(curr.data)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
    def postorder(self):
        node=self.root
        s1=[node]
        s2=[]
        while s1:
            curr=s1.pop()
            s2.append(curr)
            if curr.left:
                s1.append(curr.left)
            if curr.right:
                s1.append(curr.right)
        while s2:
            print(s2.pop().data)

    def count(self):
        c=0
        node=self.root
        stack=[node]
        while stack:
            curr=stack.pop()
            if not curr.left and not curr.right:
                c+=1
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        print(c)
    def print_all_traversal(self):
        node=self.root
        s=[(node,[node.data])]
        while s:
            curr,path=s.pop()
            if not curr.left and not curr.right:
                print(path)
            if curr.left:
                s.append((curr.left,path+[curr.left.data]))
            if curr.right:
                s.append((curr.right,path+[curr.right.data]))
           
            
    def level(self):
        node=self.root
        s=[node]
        k=[]
        l=0
        c=0
        while s: 
            if not s[l].left and not s[l].right:
                c+=1
            if s[l].left:
                s.append(s[l].left)
            if s[l].right:
                s.append(s[l].right)
            k.append(s.pop(l))
        print(c)
        for i in k:
            print(i.data,end=' ')
    def find_height(self):
        node=self.root
        st=[(0,node)]
        maxi=0
        c=1
        while st:
            c,curr=st.pop()
            if not curr.left and not curr.right:
                maxi=max(maxi,c)
            if curr.right:
                st.append((c+1,curr.right))
            if curr.left:
                st.append((c+1,curr.left))
        print(maxi)
    def find_max(self):
        node=self.root
        while node.right:
            node=node.right
        print(node.data)
    def find_all_leaf_nodes(self):
        node=self.root
        st=[node]
        while st:
            curr=st.pop()
            if not curr.left and not curr.right:
                print(curr.data)
            if curr.right:
                print(curr.right)
            if curr.left:
                st.append(curr.left)
    def lca_bst(self,p,r):
        node=self.root
        while node:
            if node.data>p and node.data>r:
                node=node.left
            elif node.data<p and node.data<r:
                node=node.right
            else:
                print(node.data)
                break
    def lcabt(self,p):
        node=self.root
        st=[(node,[node.data])]
        while st:
            curr,path=st.pop()
            if curr.data==p:
                print(path)
            if curr.right:
                st.append((curr.right,path+[curr.right.data]))
            if curr.left:
                st.append((curr.left,path+[curr.left.data]))
    def check_bal(self):
        node=self.root()
        stack=[node]
        while stack:
            curr=stack.pop()
            while curr:
                curr=curr.left
                stack.append(curr)
            curr=stack.pop()
            


        
        

            
        



        

            



obj=bst()
obj.create(10)
obj.create(8)
obj.create(7)
obj.create(9)
obj.create(12)
obj.create(11)
obj.create(13)
obj.create(15)
# obj.inorder()
# obj.preorder()
# obj.postorder()
# obj.count()
# obj.print_all_traversal()
# obj.find_height()
# obj.find_max()
# obj.find_all_leaf_nodes()
# obj.level()
obj.lca_bst(7,13)
obj.lcabt(7)
obj.lcabt(13)
obj.check_bal()