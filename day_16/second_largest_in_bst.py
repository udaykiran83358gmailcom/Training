class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self,data):
        new=Node(data)
        if self.root==None:
            self.root=new
        else:
            self.insertion(self.root,new)
    def insertion(self,root,new):
        if root.data>new.data:
            if root.left==None:
                root.left=new
            else:
                self.insertion(root.left,new)
        else:
            if root.right==None:
                root.right=new
            else:
                self.insertion(root.right,new)

    def display(self):
        # preorder
        node=self.root
        st=[node]
        while st:
            curr=st.pop() 
            print(curr.data,end=" ")
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
    def sec_lar(self):
        node=self.root
        parent=None
        while node.right:
            parent=node
            node=node.right
        if node.left:
            node=node.left
            while node.right:
                node=node.right
            print(node.data)
        else:
            print(parent.data)
    def in_order(self):
        curr=self.root
        st=[]
        ans=[]
        while st or curr:
            while curr:
                st.append(curr)
                curr=curr.left
            curr=st.pop()
            ans.append((curr.data))
            curr=curr.right
        return ans
        


            
            
obj=bst()
obj.insert(5) 
obj.insert(2)
obj.insert(8)
obj.insert(1)
obj.insert(7)
obj.display()
obj.sec_lar()
t=obj.in_order()

print()